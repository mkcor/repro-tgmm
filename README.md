# repro-tgmm
Reproduce segmentation results from open research in live imaging of mouse embryonic development at the single-cell level.

## Set up computing environment

    mkdir -p ~/envs
    python3.9 -m venv ~/envs/repro-tgmm
    source ~/envs/repro-tgmm/bin/activate
    pip install --upgrade pip
    pip install numpy==1.26.4
    pip install scikit-build

    cd ~/envs/
    git clone https://github.com/bhoeckendorf/pyklb.git
    cd pyklb/
    git checkout skbuild
    cp ~/repro-tgmm/load/pin_dep.patch .
    git am < pin_dep.patch
    pip install -v .

    cd ~/repro-tgmm/
    pip install scikit-image==0.24.0
    pip install zarr

## Workflow

    ssh mkcor@broome.cluster.recurse.com
    cd repro-tgmm/
    cd data/  # download the bioimaging data
    source ~/envs/repro-tgmm/bin/activate
    cd ../load/  # load the data into Python

## References

McDole K, Guignard L, Amat F, Berger A, Malandain G, Royer LA, Turaga SC,
Branson K, Keller PJ (2018) "*In Toto* Imaging and Reconstruction of
Post-Implantation Mouse Development at the Single-Cell Level" Cell,
175(3):859-876.e33.
DOI: [10.1016/j.cell.2018.09.031](http://doi.org/10.1016/j.cell.2018.09.031)
