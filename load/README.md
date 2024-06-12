# Load the data into Python

    mkdir -p ~/envs
    python3.7 -m venv ~/envs/read-klb
    source ~/envs/read-klb/bin/activate
    pip install --upgrade pip
    pip install scikit-build

    cd ~/envs/
    git clone https://github.com/bhoeckendorf/pyklb.git
    cd pyklb/
    git checkout skbuild
    cp ~/repro-tgmm/load/pin_dep.patch .
    git am < pin_dep.patch
    pip install -v .

    cd ~/repro-tgmm/load/
    python read_write.py
    deactivate

## References

https://github.com/bhoeckendorf/pyklb/pull/12
https://github.com/recursecenter/cluster-config/pull/59
