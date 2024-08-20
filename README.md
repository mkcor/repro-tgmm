# repro-tgmm
Reproduce segmentation results from open research in live imaging of mouse embryonic development at the single-cell level.

## Create (remote) computing environments

    mkdir -p ~/envs

    python3.9 -m venv ~/envs/load
    source ~/envs/load/bin/activate
    pip install --upgrade pip
    pip install -r requirements/load.txt
    deactivate

    python3.9 -m venv ~/envs/proc
    source ~/envs/proc/bin/activate
    pip install --upgrade pip
    pip install -r requirements/proc.txt
    deactivate

## Create (local) viewing environments

    mkdir -p ~/envs

    python3.11 -m venv ~/envs/view
    source ~/envs/view/bin/activate
    pip install --upgrade pip
    pip install -r requirements/view.txt
    deactivate

    python3.9 -m venv ~/envs/pres
    source ~/envs/pres/bin/activate
    pip install --upgrade pip
    pip install -r requirements/pres.txt
    deactivate

## Workflow

    ssh mkcor@broome.cluster.recurse.com
    cd repro-tgmm/
    cd data/
    cat README.md  # how to download the bioimaging data

    cd tgmm/
    /home/mkcor/tgmm-paper/install/bin/ProcessStack_woGPU config.md 184
    /home/mkcor/tgmm-paper/install/bin/ProcessStack_woGPU ../data/outputs/sample_frame_184_seg_conn74_rad2.bin 14 14
    cd ../

    source ~/envs/load/bin/activate
    python load/save_tgmm_seg.py .  # save result from reproducibility
    python load/read_write.py .  # convert the data into zarr
    deactivate

    source ~/envs/proc/bin/activate
    python proc/run_3d_segmentation_embryo.py .  # process data
    deactivate

    logout
    scp mkcor@broome.cluster.recurse.com:~/repro-tgmm/data/outputs/*.npz view/.
    source ~/envs/view/bin/activate
    cd view/
    python explore_seg_results.py  # compare segmentation results in napari
    deactivate

## References

McDole K, Guignard L, Amat F, Berger A, Malandain G, Royer LA, Turaga SC,
Branson K, Keller PJ (2018) "*In Toto* Imaging and Reconstruction of
Post-Implantation Mouse Development at the Single-Cell Level" Cell,
175(3):859-876.e33.
DOI: [10.1016/j.cell.2018.09.031](http://doi.org/10.1016/j.cell.2018.09.031)
