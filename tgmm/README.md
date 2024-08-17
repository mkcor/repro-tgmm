# Segment the embryo's cells with the TGMM software

TGMM stands for Tracking with Gaussian Mixture Models. The original research
involved writing code to track individual cells in the 3D images of developing
mouse embryos. The code was authored by Fernando Amat and released at:
https://bitbucket.org/fernandoamat/tgmm-paper

## Install and configure the TGMM software

We followed these instructions:
https://bitbucket.org/StatMarianne/tgmm-paper/src/1a91759d7f8bb96ba40db969e5f2f8be0f58d80d/doc/new/docs/dev-guide/building.md

On a machine with no GPU, we want to run the `ProcessStack_woGPU` executable.
Under the `build/` directory we just created, file `install_manifest.txt`
provides all the useful paths (e.g., in our case, the prefix is
`/home/mkcor/tgmm-paper/install/bin/`).

We copied the config file (which, in the `tgmm-paper` repo, is found under
`doc/new/docs/user-guide/example-config.md`) into `config.md` here, and edited
the file locations (see commit 01c21df).

## Compute the TGMM segmentation

    /home/mkcor/tgmm-paper/install/bin/ProcessStack_woGPU config.md 184

This prints step-by-step information, ending with:

    [...]
    Building dendrogram took 6 secs
    Overall hierarchical segmentation computation took 31 secs
    Writing to ../data/outputs/sample_frame_184_seg_conn74_rad2.bin
    Done writing.

## Output the TGMM segmentation

We pass tau=14 because persistanceSegmentationTau=14 in the TGMM config file,
and minSuperVoxelSzPx=14 because we changed the value of minNucleiSize from 50 to 14,
in order to detect more cells.

    /home/mkcor/tgmm-paper/install/bin/ProcessStack_woGPU ../data/outputs/sample_frame_184_seg_conn74_rad2.bin 14 14

Prints:

    ProcessStack Version list-2-gfd13c85 fd13c85
    A total of 2491 labels for tau=14
    KLB file written to ../data/outputs/sample_frame_184_seg_conn74_rad2.bin_tau14.klb

In conclusion, 2491 cells were detected.

## References

* https://bitbucket.org/fernandoamat/tgmm-paper/pull-requests/2
