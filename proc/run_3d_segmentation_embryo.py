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

im3d = im3d[:800, :2000, :2150]
sample = im3d[400:500, :, :1500]
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
print('Maximum of threshold image:', local_thresh.max())

binary_local = sample > local_thresh
np.savez_compressed('binary_local.npz', binary_local)

#####################################################################
print(f'Smooth out (binary) locally thresholded image')
print(f'# ===========================================')

smooth = ski.util.apply_parallel(
    ski.filters.gaussian,
    binary_local,
    chunks=(5, 50, 50),
    extra_keywords={'sigma': 1.5},
)

thresholds = ski.filters.threshold_multiotsu(smooth, classes=3)
regions = np.digitize(smooth, bins=thresholds)

#####################################################################
print(f'Keep nuclei as brightest of the three classes')
print(f'# ===========================================')

cells_noisy = smooth > thresholds[1]
cells = ski.morphology.opening(cells_noisy, footprint=np.ones((3, 5, 5)))
