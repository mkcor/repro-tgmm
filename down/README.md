# Download the bioimaging data

The data are available in the
[IDR](https://idr.openmicroscopy.org/webclient/?show=project-502), where the
study is registered under `idr0044-mcdole-tardislightsheet`.

As per the
[general instructions](https://idr.openmicroscopy.org/about/download.html),
the data can be downloaded using anonymous File Transfer Protocol (FTP). We
use the command-line interface (CLI).

Connect to the FTP server:

    $ ftp ftp.ebi.ac.uk

When prompted for a username, type in `ftp` or `anonymous` (with no password).
Make sure that passive mode is on:

    ftp> passive

Change the directory:

    ftp> cd /pub/databases/IDR/

List the content of the directory for the study of interest:

    ftp> ls idr0044-mcdole-tardislightsheet

Move to the directory which contains imaging data for `Embryo2`, as per the
[data catalog](https://github.com/IDR/idr0044-mcdole-tardislightsheet/blob/master/experimentA/idr0044-experimentA-filePaths.tsv):

    ftp> cd idr0044-mcdole-tardislightsheet/20180926-ftp/140813/

Move to the directory for time point 184:

    ftp> cd Mmu_E1_CAGTAG1.TM000184_timeFused_blending/

Download 3D frame:

    ftp> get SPM00_TM000184_CM00_CM01_CHN00.fusedStack.corrected.shifted.klb

Close the connection to the FTP server:

    ftp> bye

## References

https://github.com/IDR/idr.openmicroscopy.org/pull/198
