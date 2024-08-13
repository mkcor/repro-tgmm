import os
import sys

import numpy as np
import pyklb as klb
import zarr as zr

if len(sys.argv) > 1:
    pref = sys.argv[1]
else:
    pref = '..'

filename = 'SPM00_TM000184_CM00_CM01_CHN00.fusedStack.corrected.shifted.klb'
filepath = os.path.join(pref, 'data', filename)
data = klb.readfull(filepath)

conv_filename = 'frame_184.zarr'
conv_filepath = os.path.join(pref, 'data', conv_filename)
zr.save(conv_filepath, data)
print('Dataset successfully converted to Zarr format!')

sample_filename = 'sample_frame_184.klb'
sample_filepath = os.path.join(pref, 'data', sample_filename)
sample = data[400:500, :2000, :2150]
klb.writefull(np.ascontiguousarray(sample), sample_filepath)
print('Sample dataset saved back to KLB format.')
