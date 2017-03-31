# seg2raw.py
# Roberto Toro, March 2017
# find the 6 dof transformation matrix that will take the volume used to draw the
# segmentation mask into registration with the raw anatomical volume (because
# often it was transformed with an unknown transformation)
# Make sure that FSL is in your path!

import subprocess as sp
import shlex
import numpy as np
import nibabel as nib
from nilearn import plotting

sdir='/pasteur/projets/cinq/rto/data/ferret/derived-segmentation/'
rdir='/pasteur/projets/cinq/rto/data/ferret/raw-data/'
sub=[
    ['F01_Adult/seg-pial/', 'F01_31102012_MSME_TEsum_magn.nii.gz', 'F01_Adult/t2/Adult_F01_31102012/msme_11/anatomy/F01_31102012_MSME_TEsum_magn_rot.nii.gz'],
    ['F02_P0/seg-pial/', 'BF02_11012013_MGE_TEsum_magn.nii.gz', 'F02_P0/t2/BF02_11012013/anatomy/BF02_11012013_MGE_TEsum_magn_rot.nii.gz'],
    ['F03_Adult/seg-pial/', 'F03_21022013_MSME_TEsum_magn.nii.gz', 'F03_Adult/t2/F03_21022013/anatomy/F03_21022013_MSME_TEsum_magn_rot.nii.gz'],
    ['F04_Adult/seg-pial/', 'F04_01032013_MSME_TEsum_magn.nii.gz', 'F04_Adult/t2/F04_01032013/anatomy/F04_01032013_MSME_TEsum_magn_rot.nii.gz'],
    ['F05_Adult/seg-pial/', 'F05_15032013_MSME_TEsum_magn.nii.gz', 'F05_Adult/t2/F05_15032013/anatomy/F05_15032013_MSME_TEsum_magn_rot.nii.gz'],
    ['F06_P4/seg-pial/', 'P4_F06_05042013_bis_MSME_TEsum_magn.nii.gz', 'F06_P4/t2/P4_F06_05042013_bis/anatomy/P4_F06_05042013_bis_MSME_TEsum_magn_rot.nii.gz'],
    ['F07_P4/seg-pial/', 'P4_F07_12042013_MSME_TEsum_magn.nii.gz', 'F07_P4/t2/P4_F07_12042013/anatomy/P4_F07_12042013_MSME_TEsum_magn_rot.nii.gz'],
    ['F08_P4/seg-pial/', 'P4_F08_25042013b_MSME_TEsum_magn.nii.gz', 'F08_P4/t2/P4_F08_25042013b/anatomy/P4_F08_25042013b_MSME_TEsum_magn_rot.nii.gz'],
    ['F09_P4/seg-pial/', 'P4_F09_03052013_MSME_TEsum_magn.nii.gz', 'F09_P4/t2/P4_F09_03052013/anatomy/P4_F09_03052013_MSME_TEsum_magn_rot.nii.gz'],
    ['F10_P8/seg-pial/', 'P8_F10_12072013_MSME_TEsum_magn.nii.gz', 'F10_P8/t2/P8_F10_12072013/anatomy/P8_F10_12072013_MSME_TEsum_magn_rot.nii.gz'],
    ['F11_P8/seg-pial/', 'P8_F11_19072013_MSME_T2_map.nii.gz', 'F11_P8/t2/P8_F11_19072013/anatomy/P8_F11_19072013_MSME_TEsum_magn_rot.nii.gz'],
    ['F12_P16/seg-pial/', 'P16_F12_02082013_MSME_TEsum_magn.nii.gz', 'F12_P16/t2/P16_F12_02082013/anatomy/P16_F12_02082013_MSME_TEsum_magn_rot.nii.gz'],
    ['F13_P8/seg-pial/', 'P8_F13_06092013_MSME_TEsum_magn-n4.nii.gz', 'F13_P8/t2/P8_F13_06092013/anatomy/P8_F13_06092013_MSME_TEsum_magn-n4_rot.nii.gz'],
    ['F14_P8/seg-pial/', 'P8_F14_31012014_MSME_TEsum_magn.nii.gz', 'F14_P8/t2/P8_F14_31012014/anatomy/P8_F14_31012014_MSME_TEsum_magn_rot.nii.gz'],
    ['F15_P16/seg-pial/', 'P16_F15_07022014_MSME_TEsum_magn.nii.gz', 'F15_P16/t2/P16_F15_07022014/anatomy/P16_F15_07022014_MSME_TEsum_magn_rot.nii.gz'],
    ['F16_P32/seg-pial/', 'P32_F16.nii.gz', 'F16_P32/t2/P32_F16_23052014/AnalysisData/anatomy/P32_F16_23052014_MSME_TEsum_magn_rot.nii.gz'],
    ['F17_P32/seg-pial/', 'P32_F17_06062014_MSME_TEsum_magn.nii.gz', 'F17_P32/t2/P32_F17_06062014/AnalysisData/anatomy/P32_F17_06062014_MSME_TEsum_magn_rot.nii.gz'],
    ['F18_P32/seg-pial/', 'P32_F18_20062014_MSME_TEsum_magn.nii.gz', 'F18_P32/t2/P32_F18_20062014/AnalysisData/anatomy/P32_F18_20062014_MSME_TEsum_magn_rot.nii.gz'],
    ['F19_P32/seg-pial/', 'P32_F19_18072014_MSME_TEsum_magn.nii.gz', 'F19_P32/t2/P32_F19_18072014/anatomy/P32_F19_18072014_MSME_TEsum_magn_rot.nii.gz'],
    ['F20_P16/seg-pial/', 'P16_F20_25072014b_MSME_TEsum_magn.nii.gz', 'F20_P16/t2/P16_F20_25072014b/anatomy/P16_F20_25072014b_MSME_TEsum_magn_rot.nii.gz'],
    ['F21_P16/seg-pial/', 'P16_F21_01082014_MSME_TEsum_magn.nii.gz', 'F21_P16/t2/P16_F21_01082014/anatomy/P16_F21_01082014_MSME_TEsum_magn_rot.nii.gz'],
    ['F22_Adult/seg-pial/', 'P64_F22_29082014_MSME_TEsum_magn.nii.gz', 'F22_Adult/t2/P64_F22/AnalysisData/anatomy/P64_F22_29082014_MSME_TEsum_magn_rot.nii.gz'],
    ['F23_P0/seg-pial/', 'P0_F23_19092014_MSME_TEsum_magn.nii.gz', 'F23_P0/t2/AnalysisData/anatomy/P0_F23_19092014_MSME_TEsum_magn_rot.nii.gz'],
    ['F24_P0/seg-pial/', 'P0_F24_25092014_MSME_TEsum_magn_rot.nii.gz', 'F24_P0/t2/P0_F24/AnalysisData/anatomy/P0_F24_25092014_MSME_TEsum_magn_rot.nii.gz'],
    ['F25_P2/seg-pial/', 'P2_F25_31012015_MSME_TEsum_magn_rot.nii.gz', 'F25_P2/t2/P2_F25_31012015/anatomy/P2_F25_31012015_MSME_TEsum_magn_rot.nii.gz'],
    ['F26_P2/seg-pial/', 'P2_F26_27022015_MSME_TEsum_magn.nii.gz', 'F26_P2/t2/P2_F26_27022015/anatomy/P2_F26_27022015_MSME_TEsum_magn_rot.nii.gz'],
    ['F27_P2/seg-pial/', 'P2_F27_01042015_MSME_TEsum_magn.nii.gz', 'F27_P2/t2/P2_F27_01042015/anatomy/P2_F27_01042015_MSME_TEsum_magn_rot.nii.gz'],
    ['F28_P2/seg-pial/', 'P2_F28_03042015_MSME_TEsum_magn_rot.nii.gz', 'F28_P2/t2/P2_F28_03042015/anatomy/P2_F28_03042015_MSME_TEsum_magn_rot.nii.gz']
]

# display pixdim and affine diagonal to check whether they are compatible
# for row in sub:
#     ssubdir=row[0]
#     seg=row[1]
#     raw=row[2]
#     imgseg=nib.load(sdir+ssubdir+seg)
#     imgraw=nib.load(rdir+raw)
#     affseg=imgseg.affine
#     affraw=imgraw.affine
#     print("Sub: {sub}, Raw affine: {raw}, Seg affine: {seg}, Seg pixdim: {pix}".format(
#         sub=ssubdir,
#         raw=np.abs(affraw).max(axis=0)[:-1],
#         seg=np.abs(affseg).max(axis=0)[:-1],
#         pix=imgseg.header.get_zooms()
#     ))

# make left/right flipped versions of the original anatomical references in the
# segmentation vramonz files (seg-raw)
# flip=np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
# for row in sub:
#     ssubdir=row[0];
#     seg=row[1];
#     raw=row[2];
#     img=nib.load(sdir+ssubdir+seg);
#     aff=img.affine.dot(flip);
#     img.affine[:]=aff;
#     nib.nifti1.save(img,sdir+ssubdir+'flip_'+seg);

# align the raw structural to the seg-raw, straight and flipped
# for row in sub:
#     ssubdir=row[0];
#     seg=row[1];
#     raw=row[2];
#     
#     # linearly register seg to raw
#     command = """flirt
#         -in {sdir}{ssubdir}{seg}
#         -ref {rdir}{raw}
#         -out {sdir}{ssubdir}seg2raw
#         -omat {sdir}{ssubdir}seg2raw.mat
#         -searchrx -180 180
#         -searchry -180 180
#         -searchrz -180 180
#         -dof 7
#         -verbose 1
#     """.format(
#         sdir=sdir,
#         ssubdir=ssubdir,
#         seg=seg,
#         rdir=rdir,
#         raw=raw
#     )
#     args = shlex.split(command)
#     print args
#     print sp.check_output(args)
# 
#     # linearly register flip_seg to raw
#     command = """flirt
#         -in {sdir}{ssubdir}flip_{seg}
#         -ref {rdir}{raw}
#         -out {sdir}{ssubdir}flip_seg2raw
#         -omat {sdir}{ssubdir}flip_seg2raw.mat
#         -searchrx -180 180
#         -searchry -180 180
#         -searchrz -180 180
#         -dof 7
#         -verbose 1
#     """.format(
#         sdir=sdir,
#         ssubdir=ssubdir,
#         seg=seg,
#         rdir=rdir,
#         raw=raw
#     )
#     args = shlex.split(command)
#     print args
#     print sp.check_output(args)
#     
#     # take a picture
#     plotting.plot_anat("{sdir}{ssubdir}seg2raw.nii.gz".format(sdir=sdir,ssubdir=ssubdir,seg=seg),output_file="seg.png", draw_cross=False,title="+seg",cut_coords=(0.5,0.5,0.5));
#     plotting.plot_anat("{sdir}{ssubdir}flip_seg2raw.nii.gz".format(sdir=sdir,ssubdir=ssubdir,seg=seg),output_file="flip_seg.png", draw_cross=False,title="-seg",cut_coords=(0.5,0.5,0.5));
#     plotting.plot_anat("{rdir}{raw}".format(rdir=rdir,raw=raw),output_file="raw.png", draw_cross=False, title="raw",cut_coords=(0.5,0.5,0.5));
#     command = "montage -geometry '1x1+0+0<' -tile 1x3 seg.png flip_seg.png raw.png {sdir}{ssubdir}{seg}.segraw.png".format(sdir=sdir,ssubdir=ssubdir,seg=seg);
#     print sp.check_output(shlex.split(command))
#     command = "rm seg.png flip_seg.png raw.png";
#     print sp.check_output(shlex.split(command))

# make left/right flipped versions of the masks in the
# segmentation vramonz files (mask)
# flip=np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
# for row in sub:
#     ssubdir=row[0];
#     seg=row[1];
#     mask=seg.split(".")[0]+'.sel.nii.gz'
#     raw=row[2];
#     print(sdir+ssubdir+mask)
#     img=nib.load(sdir+ssubdir+mask);
#     aff=img.affine.dot(flip);
#     img.affine[:]=aff;
#     nib.nifti1.save(img,sdir+ssubdir+'flip_'+mask);

# apply the affine transformations from the previous step to the masks
for row in sub:
    ssubdir=row[0];
    seg=row[1];
    mask=seg.split(".")[0]+'.sel.nii.gz'
    raw=row[2];
    
    # apply linear registration to mask
    command = """flirt
        -in {sdir}{ssubdir}{mask}
        -init {sdir}{ssubdir}seg2raw.mat
        -ref {rdir}{raw}
        -applyxfm
        -out {sdir}{ssubdir}seg2raw.sel
        -verbose 1
    """.format(
        sdir=sdir,
        ssubdir=ssubdir,
        mask=mask,
        rdir=rdir,
        raw=raw
    )
    args = shlex.split(command)
    print args
    print sp.check_output(args)

    # apply linear registration to flip_mask
    command = """flirt
        -in {sdir}{ssubdir}flip_{mask}
        -init {sdir}{ssubdir}flip_seg2raw.mat
        -ref {rdir}{raw}
        -applyxfm
        -out {sdir}{ssubdir}flip_seg2raw.sel
        -verbose 1
    """.format(
        sdir=sdir,
        ssubdir=ssubdir,
        mask=mask,
        rdir=rdir,
        raw=raw
    )
    args = shlex.split(command)
    print args
    print sp.check_output(args)
