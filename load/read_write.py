import os

import numpy as np
import pyklb as klb
import zarr as zr

filename = 'SPM00_TM000184_CM00_CM01_CHN00.fusedStack.corrected.shifted.klb'
filepath = os.path.join("..", "data", filename)
data = klb.readfull(filepath)

conv_filename = 'frame_184.zarr'
conv_filepath = os.path.join("..", "data", conv_filename)
zr.save(conv_filepath, data)
