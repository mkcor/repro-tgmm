import numpy as np
import napari

sample = np.load('sample.npz')['arr_0']

viewer = napari.Viewer()
image_layer = viewer.add_image(sample)

# start the event loop and show the viewer
napari.run()
