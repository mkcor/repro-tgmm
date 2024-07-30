# repro-tgmm
Reproduce segmentation results from open research in live imaging of mouse embryonic development at the single-cell level.

## Create computing environments

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

    python3.9 -m venv ~/envs/pres
    source ~/envs/pres/bin/activate
    pip install --upgrade pip
    pip install -r requirements/pres.txt
    deactivate

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
