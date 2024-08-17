import numpy as np
import napari

sample = np.load('sample.npz')['arr_0']
sample_slice = sample[50, :, :]
cells = np.load('cells.npz')['arr_0']
proc_seg = np.load('proc_seg.npz')['arr_0']
tgmm_seg = np.load('tgmm_seg.npz')['arr_0']

viewer = napari.Viewer()
image_layer = viewer.add_image(sample_slice, name='raw image')
tgmm_layer = viewer.add_labels(tgmm_seg, name='reproducibility')
proc_layer = viewer.add_labels(proc_seg, name='replication')
cells_layer = viewer.add_image(cells, name='cells before watershed')

# start the event loop and show the viewer
napari.run()
