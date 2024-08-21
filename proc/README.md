# Segment the embryo's cells with Scientific Python

    source ~/envs/proc/bin/activate
    python run_3d_segmentation_embryo.py

which prints:

```bash
Load 3D image data
# ================
The shape of the image is: (847, 2048, 2190)
The shape of the sample is: (100, 2000, 2150)
Saved data sample at ../data/outputs/sample.npz
Apply local thresholding
# ======================
Maximum of threshold image: 1326.8555194101925
Smooth out (binary) locally thresholded image
# ===========================================
Apply global thresholding
# =======================
Keep nuclei as brightest of the three classes
# ===========================================
Saved detected cells before watershed at ../data/outputs/cells.npz
Use watershed algorithm
# =====================
Number of segmented cells: 7040
Saved (replicated) segmentation result at ../data/outputs/proc_seg.npz
```

## References

* https://github.com/scikit-image/scikit-image/pull/7309
* https://gitlab.com/scikit-image/data/-/merge_requests/24
