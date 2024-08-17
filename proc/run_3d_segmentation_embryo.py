"""
==================================================
Segment 3D image sample of developing mouse embryo
==================================================

In this example, we look at a microscopy image of a developing mouse embryo.
We use sample data from [1]_, more precisely from embryo B at time point 184.
"""
import os
import sys

import numpy as np
import scipy as sp

import dask.array as da
import skimage as ski
import zarr as zr


# Use proper prefix to locate data files
if len(sys.argv) > 1:
    pref = sys.argv[1]
else:
    pref = '..'

#####################################################################
print(f'Load 3D image data')
print(f'# ================')

filename = 'frame_184.zarr'
filepath = os.path.join(pref, 'data', filename)
im3d = zr.open(filepath)
print(f'The shape of the image is: {im3d.shape}')

#####################################################################
# Trim 3D image so that each axis is a multiple of 50.

#sample = im3d[:800, :2000, :2150]
sample = im3d[400:500, :2000, :2150]
del im3d
print(f'The shape of the sample is: {sample.shape}')

#####################################################################
print(f'Apply local thresholding')
print(f'# ======================')

# # global thresholding
# def binary_global(x):
#     global_thresh = ski.filters.threshold_otsu(x)
#     return (x > global_thresh)
#
# gl = ski.util.apply_parallel(binary_global, im3d, chunks=50)

local_thresh = ski.util.apply_parallel(
    ski.filters.threshold_local,
    sample,
    chunks=(5, 50, 50),
    extra_keywords={'block_size': 31},
    dtype='float64'
)
print(f'Maximum of threshold image: {local_thresh.max()}')

binary_local = sample > local_thresh
del sample, local_thresh

#####################################################################
print(f'Smooth out (binary) locally thresholded image')
print(f'# ===========================================')

smooth = ski.util.apply_parallel(
    ski.filters.gaussian,
    binary_local,
    chunks=(5, 50, 50),
    extra_keywords={'sigma': 1.5},
    dtype='float64'
)
del binary_local

#####################################################################
print(f'Apply global thresholding')
print(f'# =======================')

thresholds = ski.filters.threshold_multiotsu(smooth, classes=3)

#####################################################################
print(f'Keep nuclei as brightest of the three classes')
print(f'# ===========================================')

cells_noisy = smooth > thresholds[1]
del smooth, thresholds
cells = ski.morphology.opening(cells_noisy, footprint=np.ones((3, 5, 5)))
del cells_noisy

#####################################################################
print(f'Use watershed algorithm')
print(f'# =====================')

distance = ski.util.apply_parallel(
    sp.ndimage.distance_transform_edt,
    cells,
    chunks=(5, 50, 50),
    dtype='float64'
)
local_max_coords = ski.feature.peak_local_max(
    distance, min_distance=14, exclude_border=False
)
local_max_mask = np.zeros(distance.shape, dtype=bool)
local_max_mask[tuple(local_max_coords.T)] = True
del local_max_coords
markers = ski.measure.label(local_max_mask)
del local_max_mask

d = da.from_array(distance, chunks=(5, 50, 50))
c = da.from_array(cells, chunks=(5, 50, 50))
m = da.from_array(markers, chunks=(5, 50, 50))
f = da.map_blocks(
    lambda a, b, c: ski.segmentation.watershed(a, markers=b, mask=c),
    -d,
    m,
    c,
    dtype='int32'
)
seg = f.compute()
print('Number of segmented cells:', np.max(seg))
