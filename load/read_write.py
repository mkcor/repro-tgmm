import os

import numpy as np
import pyklb as klb

filename = 'SPM00_TM000184_CM00_CM01_CHN00.fusedStack.corrected.shifted.klb'
filepath = os.path.join("..", "down", filename)
data = klb.readfull(filepath)
np.savez_compressed('frame_184.npz', data)
