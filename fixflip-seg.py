# seg2raw.py
# Roberto Toro, March 2017
# find the 6 dof transformation matrix that will take the volume used to draw the
# segmentation mask into registration with the raw anatomical volume (because
# often it was transformed with an unknown transformation)
# Make sure that FSL is in your path!

import subprocess as sp, shlex

sdir='/pasteur/projets/cinq/rto/data/ferret/derived-segmentation/'
rdir='/pasteur/projets/cinq/rto/data/ferret/raw-data/'
sub=[
   [0, 'F01_Adult/seg-pial/', 'F01_31102012_MSME_TEsum_magn.nii.gz', 'F01_Adult/t2/Adult_F01_31102012/msme_11/anatomy/F01_31102012_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F02_P0/seg-pial/', 'BF02_11012013_MGE_TEsum_magn.nii.gz', 'F02_P0/t2/BF02_11012013/anatomy/BF02_11012013_MGE_TEsum_magn_rot.nii.gz'],
   [1, 'F03_Adult/seg-pial/', 'F03_21022013_MSME_TEsum_magn.nii.gz', 'F03_Adult/t2/F03_21022013/anatomy/F03_21022013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F04_Adult/seg-pial/', 'F04_01032013_MSME_TEsum_magn.nii.gz', 'F04_Adult/t2/F04_01032013/anatomy/F04_01032013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F05_Adult/seg-pial/', 'F05_15032013_MSME_TEsum_magn.nii.gz', 'F05_Adult/t2/F05_15032013/anatomy/F05_15032013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F06_P4/seg-pial/', 'P4_F06_05042013_bis_MSME_TEsum_magn.nii.gz', 'F06_P4/t2/P4_F06_05042013_bis/anatomy/P4_F06_05042013_bis_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F07_P4/seg-pial/', 'P4_F07_12042013_MSME_TEsum_magn.nii.gz', 'F07_P4/t2/P4_F07_12042013/anatomy/P4_F07_12042013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F08_P4/seg-pial/', 'P4_F08_25042013b_MSME_TEsum_magn.nii.gz', 'F08_P4/t2/P4_F08_25042013b/anatomy/P4_F08_25042013b_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F09_P4/seg-pial/', 'P4_F09_03052013_MSME_TEsum_magn.nii.gz', 'F09_P4/t2/P4_F09_03052013/anatomy/P4_F09_03052013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F10_P8/seg-pial/', 'P8_F10_12072013_MSME_TEsum_magn.nii.gz', 'F10_P8/t2/P8_F10_12072013/anatomy/P8_F10_12072013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F11_P8/seg-pial/', 'P8_F11_19072013_MSME_T2_map.nii.gz', 'F11_P8/t2/P8_F11_19072013/maps/P8_F11_19072013_MSME_T2_map_rot.nii.gz'],
   [1, 'F12_P16/seg-pial/', 'P16_F12_02082013_MSME_TEsum_magn.nii.gz', 'F12_P16/t2/P16_F12_02082013/anatomy/P16_F12_02082013_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F13_P8/seg-pial/', 'P8_F13_06092013_MSME_TEsum_magn-n4.nii.gz', 'F13_P8/t2/P8_F13_06092013/anatomy/P8_F13_06092013_MSME_TEsum_magn-n4_rot.nii.gz'],
   [1, 'F14_P8/seg-pial/', 'P8_F14_31012014_MSME_TEsum_magn.nii.gz', 'F14_P8/t2/P8_F14_31012014/anatomy/P8_F14_31012014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F15_P16/seg-pial/', 'P16_F15_07022014_MSME_TEsum_magn.nii.gz', 'F15_P16/t2/P16_F15_07022014/anatomy/P16_F15_07022014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F16_P32/seg-pial/', 'P32_F16.nii.gz', 'F16_P32/t2/P32_F16_23052014/AnalysisData/anatomy/P32_F16_23052014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F17_P32/seg-pial/', 'P32_F17_06062014_MSME_TEsum_magn.nii.gz', 'F17_P32/t2/P32_F17_06062014/AnalysisData/anatomy/P32_F17_06062014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F18_P32/seg-pial/', 'P32_F18_20062014_MSME_TEsum_magn.nii.gz', 'F18_P32/t2/P32_F18_20062014/AnalysisData/anatomy/P32_F18_20062014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F19_P32/seg-pial/', 'P32_F19_18072014_MSME_TEsum_magn.nii.gz', 'F19_P32/t2/P32_F19_18072014/anatomy/P32_F19_18072014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F20_P16/seg-pial/', 'P16_F20_25072014b_MSME_TEsum_magn.nii.gz', 'F20_P16/t2/P16_F20_25072014b/anatomy/P16_F20_25072014b_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F21_P16/seg-pial/', 'P16_F21_01082014_MSME_TEsum_magn.nii.gz', 'F21_P16/t2/P16_F21_01082014/anatomy/P16_F21_01082014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F22_Adult/seg-pial/', 'P64_F22_29082014_MSME_TEsum_magn.nii.gz', 'F22_Adult/t2/P64_F22/AnalysisData/anatomy/P64_F22_29082014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F23_P0/seg-pial/', 'P0_F23_19092014_MSME_TEsum_magn.nii.gz', 'F23_P0/t2/AnalysisData/anatomy/P0_F23_19092014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F24_P0/seg-pial/', 'P0_F24_25092014_MSME_TEsum_magn_rot.nii.gz', 'F24_P0/t2/P0_F24/AnalysisData/anatomy/P0_F24_25092014_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F25_P2/seg-pial/', 'P2_F25_31012015_MSME_TEsum_magn.nii.gz', 'F25_P2/t2/P2_F25_31012015/anatomy/P2_F25_31012015_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F26_P2/seg-pial/', 'P2_F26_27022015_MSME_TEsum_magn.nii.gz', 'F26_P2/t2/P2_F26_27022015/anatomy/P2_F26_27022015_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F27_P2/seg-pial/', 'P2_F27_01042015_MSME_TEsum_magn.nii.gz', 'F27_P2/t2/P2_F27_01042015/anatomy/P2_F27_01042015_MSME_TEsum_magn_rot.nii.gz'],
   [1, 'F28_P2/seg-pial/', 'P2_F28_03042015_MSME_TEsum_magn_rot.nii.gz', 'F28_P2/t2/P2_F28_03042015/anatomy/P2_F28_03042015_MSME_TEsum_magn_rot.nii.gz']
]
for row in sub:
    flip=row[0];
    ssubdir=row[1];
    seg=row[2];
    raw=row[3];
    
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

    command = "slicer {sdir}{ssubdir}seg2raw.nii.gz -a seg.png -L".format(
        sdir=sdir,
        ssubdir=ssubdir,
        seg=seg
    )
    print sp.check_output(shlex.split(command))

    command = "slicer {rdir}{raw} -a raw.png -L ".format(
        rdir=rdir,
        raw=raw
    )
    print sp.check_output(shlex.split(command))

    command = "montage -geometry '1x1+0+0<' -tile 1x2 seg.png raw.png {sdir}{ssubdir}{seg}.segraw.png".format(sdir=sdir,ssubdir=ssubdir,seg=seg);
    print sp.check_output(shlex.split(command))

    command = "rm seg.png raw.png";
    print sp.check_output(shlex.split(command))
