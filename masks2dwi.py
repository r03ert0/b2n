import subprocess as sp
import shlex
import nibabel as nib
import numpy as np

sub=[
    ['F01_Adult/seg-pial/', 'F01_31102012_MSME_TEsum_magn_rot.nii.gz', 'F01_Adult/dti/nii/F01_Adult_rot.nii.gz'],
    ['F02_P0/seg-pial/flip_', 'BF02_11012013_MSME_TEsum_magn_rot.nii.gz', 'F02_P0/dti/nii/F02_P0_rot.nii.gz'],
    ['F03_Adult/seg-pial/flip_', 'F03_21022013_MSME_TEsum_magn_rot.nii.gz', 'F03_Adult/dti/nii/F03_Adult_rot.nii.gz'],
    ['F04_Adult/seg-pial/flip_', 'F04_01032013_MSME_TEsum_magn_rot.nii.gz', 'F04_Adult/dti/nii/F04_Adult_rot.nii.gz'],
    ['F05_Adult/seg-pial/flip_', 'F05_15032013_MSME_TEsum_magn_rot.nii.gz', 'F05_Adult/dti/nii/F05_Adult_rot.nii.gz'],
    ['F06_P4/seg-pial/flip_', 'P4_F06_05042013_bis_MSME_TEsum_magn_rot.nii.gz', 'F06_P4/dti/nii/F06_P4_rot.nii.gz'],
    ['F07_P4/seg-pial/flip_', 'P4_F07_12042013_MSME_TEsum_magn_rot.nii.gz', 'F07_P4/dti/nii/F07_P4_rot.nii.gz'],
    ['F08_P4/seg-pial/flip_', 'P4_F08_25042013b_MSME_TEsum_magn_rot.nii.gz', 'F08_P4/dti/nii/F08_P4_rot.nii.gz'],
    ['F09_P4/seg-pial/flip_', 'P4_F09_03052013_MSME_TEsum_magn_rot.nii.gz', 'F09_P4/dti/nii/F09_P4_rot.nii.gz'],
    ['F10_P8/seg-pial/flip_', 'P8_F10_12072013_MSME_TEsum_magn_rot.nii.gz', 'F10_P8/dti/nii/F10_P8_rot.nii.gz'],
    ['F11_P8/seg-pial/flip_', 'P8_F11_19072013_MSME_T2_map.nii.gz', 'F11_P8/dti/nii/F11_P8_rot.nii.gz'],
    ['F12_P16/seg-pial/flip_', 'P16_F12_02082013_MSME_TEsum_magn_rot.nii.gz', 'F12_P16/dti/nii/F12_P16_rot.nii.gz'],
    ['F13_P8/seg-pial/flip_', 'P8_F13_06092013_MSME_TEsum_magn_rot-n4.nii.gz', 'F13_P8/dti/nii/F13_P8_rot.nii.gz'],
    ['F14_P8/seg-pial/flip_', 'P8_F14_31012014_MSME_TEsum_magn_rot.nii.gz', 'F14_P8/dti/nii/F14_P8_rot.nii.gz'],
    ['F15_P16/seg-pial/flip_', 'P16_F15_07022014_MSME_TEsum_magn_rot.nii.gz', 'F15_P16/dti/nii/F15_P16_rot.nii.gz'],
    ['F16_P32/seg-pial/flip_', 'P32_F16_rot.nii.gz', 'F16_P32/dti/nii/F16_P32_rot.nii.gz'],
    ['F17_P32/seg-pial/flip_', 'P32_F17_06062014_MSME_TEsum_magn_rot.nii.gz', 'F17_P32/dti/nii/F17_P32_rot.nii.gz'],
    ['F18_P32/seg-pial/flip_', 'P32_F18_20062014_MSME_TEsum_magn_rot.nii.gz', 'F18_P32/dti/nii/F18_P32_rot.nii.gz'],
    ['F19_P32/seg-pial/', 'P32_F19_18072014_MSME_TEsum_magn_rot.nii.gz', 'F19_P32/dti/nii/F19_P32_rot.nii.gz'],
    ['F20_P16/seg-pial/', 'P16_F20_25072014b_MSME_TEsum_magn_rot.nii.gz', 'F20_P16/dti/nii/F20_P16_rot.nii.gz'],
    ['F21_P16/seg-pial/flip_', 'P16_F21_01082014_MSME_TEsum_magn_rot.nii.gz', 'F21_P16/dti/nii/F21_P16_rot.nii.gz'],
    ['F22_Adult/seg-pial/flip_', 'P64_F22_29082014_MSME_TEsum_magn_rot.nii.gz', 'F22_Adult/dti/nii/F22_Adult_rot.nii.gz'],
    ['F23_P0/seg-pial/flip_', 'P0_F23_19092014_MSME_TEsum_magn_rot.nii.gz', 'F23_P0/dti/nii/F23_P0_rot.nii.gz'],
    ['F24_P0/seg-pial/', 'P0_F24_25092014_MSME_TEsum_magn_rot.nii.gz', 'F24_P0/dti/nii/F24_P0_rot.nii.gz'],
    ['F25_P2/seg-pial/', 'P2_F25_31012015_MSME_TEsum_magn_rot.nii.gz', 'F25_P2/dti/nii/F25_P2_rot.nii.gz'],
    ['F26_P2/seg-pial/flip_', 'P2_F26_27022015_MSME_TEsum_magn_rot.nii.gz', 'F26_P2/dti/nii/F26_P2_rot.nii.gz'],
    ['F27_P2/seg-pial/flip_', 'P2_F27_01042015_MSME_TEsum_magn_rot.nii.gz', 'F27_P2/dti/nii/F27_P2_rot.nii.gz'],
    ['F28_P2/seg-pial/', 'P2_F28_03042015_MSME_TEsum_magn_rot.nii.gz', 'F28_P2/dti/nii/F28_P2_rot.nii.gz']
]
sdir='/pasteur/projets/cinq/rto/data/ferret/derived-segmentation/'
rdir='/pasteur/projets/cinq/rto/data/ferret/raw-data/'
for row in sub:
    ssubdir=row[0];
    seg=row[1];
    mask=seg.split(".")[0]+'.sel.nii.gz'
    raw=row[2];

    command = """flirt
        -ref {rdir}{raw}
        -in {sdir}{ssubdir}seg2raw.nii.gz
        -omat {sdir}{ssubdir}seg2dwi.mat
        -out {sdir}{ssubdir}seg2dwi.nii.gz
        -usesqform
    """.format(
        sdir=sdir,
        ssubdir=ssubdir,
        rdir=rdir,
        raw=raw
    )
    try:
        args = shlex.split(command)
        print args
        print sp.check_output(args)
    except:
        print("ERROR: Could not execute the command "+command);

    command = """flirt
        -ref {rdir}{raw}
        -in {sdir}{ssubdir}seg2raw.sel.nii.gz
        -init {sdir}{ssubdir}seg2dwi.mat
        -out {sdir}{ssubdir}seg2dwi.sel.nii.gz
        -applyxfm
    """.format(
        sdir=sdir,
        ssubdir=ssubdir,
        rdir=rdir,
        raw=raw
    )
    try:
        args = shlex.split(command)
        print args
        print sp.check_output(args)
    except:
        print("ERROR: Could not execute the command "+command);
