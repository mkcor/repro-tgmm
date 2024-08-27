import numpy as np
import napari

sample = np.load('sample.npz')['arr_0']
sample_slice = sample[50, :, :]
cells = np.load('cells.npz')['arr_0']
proc_seg = np.load('proc_seg.npz')['arr_0']
tgmm_seg = np.load('tgmm_seg.npz')['arr_0']

viewer = napari.Viewer()
image_layer = viewer.add_image(
    sample_slice,
    blending='additive',
    contrast_limits=(0, 350),
    name='raw image'
)
tgmm_layer = viewer.add_labels(
    tgmm_seg,
    blending='translucent',
    name='reproducibility'
)
cells_layer = viewer.add_image(
    cells,
    blending='additive',
    name='cells before watershed'
)
proc_layer = viewer.add_labels(
    proc_seg,
    blending='translucent',
    name='replication'
)
viewer.grid.enabled = True
viewer.grid.stride = 2
viewer.dims.current_step = (50, 999, 1074)

# start the event loop and show the viewer
napari.run()
