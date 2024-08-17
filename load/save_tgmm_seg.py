import os
import sys

import numpy as np
import pyklb as klb

if len(sys.argv) > 1:
    pref = sys.argv[1]
else:
    pref = '..'

filename = 'sample_frame_184_seg_conn74_rad2.bin_tau14.klb'
filepath = os.path.join(pref, 'data', 'outputs', filename)
data = klb.readfull(filepath)

conv_filename = 'tgmm_seg.npz'
conv_filepath = os.path.join(pref, 'data', 'outputs', conv_filename)
np.savez_compressed(conv_filepath, data)
print(f'Saved (reproduced) TGMM segmentation at {conv_filepath}')
