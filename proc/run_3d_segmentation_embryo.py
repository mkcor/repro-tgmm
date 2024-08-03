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
# View 3D image data
# ==================

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
# Apply local thresholding
# ========================

# # global thresholding
# def binary_global(x):
#     global_thresh = ski.filters.threshold_otsu(x)
#     return (x > global_thresh)
#
# gl = ski.util.apply_parallel(binary_global, im3d, chunks=50)

local_thresh = ski.util.apply_parallel(
    ski.filters.threshold_local,
    sample,
    chunks=50,
    extra_keywords={'block_size': 31},
    dtype='uint16'
)
print('Maximum of threshold image:', local_thresh.max())
