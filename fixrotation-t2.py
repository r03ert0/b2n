import nibabel as nib
import numpy as np

def rotate(src,dst,rot):
    img=nib.load(src)
    print("orig:"+str(np.linalg.det(img.affine)))
    img.affine[:]=rot.dot(img.affine)
    nib.nifti1.save(img,dst)

sub=[
     [1,'F02_P0/t2/BF02_11012013/anatomy/BF02_11012013_MGE_TEsum_magn.nii.gz'],
     [1,'F02_P0/t2/BF02_11012013/anatomy/BF02_11012013_MSME_TEsum_magn.nii.gz'],
     [2,'F19_P32/t2/P32_F19/anatomy/P32_F19_18072014_MGE_TEsum_magn.nii.gz'],
     [2,'F19_P32/t2/P32_F19/anatomy/P32_F19_18072014_MSME_TEsum_magn.nii.gz'],
     [1,'F23_P0/t2/AnalysisData/anatomy/P0_F23_19092014_MSME_TEsum_magn.nii.gz'],
     [1,'F23_P0/t2/AnalysisData/anatomy/P0_F23_19092014_MGE_TEsum_magn.nii.gz'],
     [1,'F23_P0/t2/RecoData/anatomy_msme_5/P0_F23_19092014_MSME_TEsum_magn.nii.gz'],
     [1,'F23_P0/t2/RecoData/anatomy_mge_6/P0_F23_19092014_MGE_TEsum_magn.nii.gz'],
     [3,'F07_P4/t2/P4_F07_12042013/anatomy/P4_F07_12042013_MGE_TEsum_magn.nii.gz'],
     [3,'F07_P4/t2/P4_F07_12042013/anatomy/P4_F07_12042013_MSME_TEsum_magn.nii.gz'],
     [1,'F03_Adult/t2/F03_21022013/anatomy/F03_21022013_MGE_TEsum_magn.nii.gz'],
     [1,'F03_Adult/t2/F03_21022013/anatomy/F03_21022013_MSME_TEsum_magn.nii.gz'],
     [3,'F15_P16/t2/P16_F15_07022014/anatomy/P16_F15_07022014_MGE_TEsum_magn.nii.gz'],
     [3,'F15_P16/t2/P16_F15_07022014/anatomy/P16_F15_07022014_MSME_TEsum_magn-n4.nii.gz'],
     [3,'F15_P16/t2/P16_F15_07022014/anatomy/P16_F15_07022014_MSME_TEsum_magn.nii.gz'],
     [3,'F24_P0/t2/P0_F24/AnalysisData/anatomy/P0_F24_25092014_MGE_TEsum_magn.nii.gz'],
     [3,'F24_P0/t2/P0_F24/AnalysisData/anatomy/P0_F24_25092014_MSME_TEsum_magn.nii.gz'],
     [3,'F24_P0/t2/P0_F24/RecoData/anatomy_msme_6/P0_F24_25092014_MSME_TEsum_magn.nii.gz'],
     [3,'F24_P0/t2/P0_F24/RecoData/anatomy_mge_7/P0_F24_25092014_MGE_TEsum_magn.nii.gz'],
     [1,'F06_P4/t2/P4_F06_05042013_bis/anatomy/P4_F06_05042013_bis_MSME_TEsum_magn.nii.gz'],
     [1,'F06_P4/t2/P4_F06_05042013_bis/anatomy/P4_F06_05042013_bis_MGE_TEsum_magn.nii.gz'],
     [3,'F05_Adult/t2/F05_15032013/anatomy/F05_15032013_MGE_TEsum_magn.nii.gz'],
     [3,'F05_Adult/t2/F05_15032013/anatomy/F05_15032013_MSME_TEsum_magn.nii.gz'],
     [3,'F12_P16/t2/P16_F12_02082013/anatomy/P16_F12_02082013_MSME_TEsum_magn.nii.gz'],
     [3,'F12_P16/t2/P16_F12_02082013/anatomy/P16_F12_02082013_MGE_TEsum_magn.nii.gz'],
     [0,'F20_P16/t2/P16_F20_25072014b/anatomy/P16_F20_25072014b_MSME_TEsum_magn.nii.gz'],
     [0,'F20_P16/t2/P16_F20_25072014b/anatomy/P16_F20_25072014b_MGE_TEsum_magn.nii.gz'],
     [1,'F13_P8/t2/P8_F13_06092013/anatomy/P8_F13_06092013_MGE_TEsum_magn.nii.gz'],
     [1,'F13_P8/t2/P8_F13_06092013/anatomy/P8_F13_06092013_MSME_TEsum_magn.nii.gz'],
     [1,'F13_P8/t2/P8_F13_06092013/anatomy/P8_F13_06092013_MSME_TEsum_magn-n4.nii.gz'],
     [3,'F18_P32/t2/P32_F18_20062014/AnalysisData/anatomy/P32_F18_20062014_MSME_TEsum_magn.nii.gz'],
     [3,'F18_P32/t2/P32_F18_20062014/AnalysisData/anatomy/P32_F18_20062014_MGE_TEsum_magn.nii.gz'],
     [3,'F18_P32/t2/P32_F18_20062014/RecoData/anatomy_msme_6/P32_F18_20062014_MSME_TEsum_magn.nii.gz'],
     [3,'F18_P32/t2/P32_F18_20062014/RecoData/anatomy_mge_5/P32_F18_20062014_MGE_TEsum_magn.nii.gz'],
     [1,'F14_P8/t2/P8_F14_31012014/anatomy/P8_F14_31012014_MGE_TEsum_magn.nii.gz'],
     [1,'F14_P8/t2/P8_F14_31012014/anatomy/P8_F14_31012014_MSME_TEsum_magn.nii.gz'],
     [1,'F14_P8/t2/P8_F14_31012014/anatomy/P8_F14_31012014_MSME_TEsum_magn-n4.nii.gz'],
     [1,'F27_P2/t2/P2_F27_01042015/anatomy/P2_F27_01042015_MGE_TEsum_magn.nii.gz'],
     [1,'F27_P2/t2/P2_F27_01042015/anatomy/P2_F27_01042015_MSME_TEsum_magn.nii.gz'],
     [3,'F26_P2/t2/P2_F26_27022015/anatomy/P2_F26_27022015_MSME_TEsum_magn.nii.gz'],
     [3,'F26_P2/t2/P2_F26_27022015/anatomy/P2_F26_27022015_MGE_TEsum_magn.nii.gz'],
     [3,'F28_P2/t2/P2_F28_03042015/anatomy/P2_F28_03042015_MGE_TEsum_magn.nii.gz'],
     [3,'F28_P2/t2/P2_F28_03042015/anatomy/P2_F28_03042015_MSME_TEsum_magn.nii.gz'],
     [1,'F16_P32/t2/P32_F16_23052014/AnalysisData/anatomy/P32_F16_23052014_MSME_TEsum_magn.nii.gz'],
     [1,'F16_P32/t2/P32_F16_23052014/AnalysisData/anatomy/P32_F16_23052014_MGE_TEsum_magn.nii.gz'],
     [1,'F16_P32/t2/P32_F16_23052014/RecoData/anatomy_msme_6/P32_F16_23052014_MSME_TEsum_magn.nii.gz'],
     [1,'F16_P32/t2/P32_F16_23052014/RecoData/anatomy_mge_5/P32_F16_23052014_MGE_TEsum_magn.nii.gz'],
     [1,'F11_P8/t2/P8_F11_19072013/anatomy/P8_F11_19072013_MSME_TEsum_magn.nii.gz'],
     [1,'F11_P8/t2/P8_F11_19072013/anatomy/P8_F11_19072013_MGE_TEsum_magn.nii.gz'],
     [1,'F04_Adult/t2/F04_01032013/anatomy/F04_01032013_MSME_TEsum_magn.nii.gz'],
     [1,'F04_Adult/t2/F04_01032013/anatomy/F04_01032013_MGE_TEsum_magn.nii.gz'],
     [1,'F10_P8/t2/P8_F10_12072013/anatomy/P8_F10_12072013_MGE_TEsum_magn.nii.gz'],
     [1,'F10_P8/t2/P8_F10_12072013/anatomy/P8_F10_12072013_MSME_TEsum_magn.nii.gz'],
     [3,'F08_P4/t2/P4_F08_25042013b/anatomy/P4_F08_25042013b_MSME_TEsum_magn.nii.gz'],
     [3,'F08_P4/t2/P4_F08_25042013b/anatomy/P4_F08_25042013b_MGE_TEsum_magn.nii.gz'],
     [1,'F09_P4/t2/P4_F09_03052013/anatomy/P4_F09_03052013_MGE_TEsum_magn.nii.gz'],
     [1,'F09_P4/t2/P4_F09_03052013/anatomy/P4_F09_03052013_MSME_TEsum_magn.nii.gz'],
     [0,'F01_Adult/t2/Adult_F01_31102012/mge_12/anatomy/F01_31102012_MGE_TEsum_magn.nii.gz'],
     [4,'F01_Adult/t2/Adult_F01_31102012/mge_14/anatomy/F01_31102012_MGE_TEsum_magn.nii.gz']
     [0,'F01_Adult/t2/Adult_F01_31102012/msme_8/anatomy/F01_31102012_MSME_TEsum_magn.nii.gz'],
     [0,'F01_Adult/t2/Adult_F01_31102012/mge_13/anatomy/F01_31102012_MGE_TEsum_magn.nii.gz'],
     [0,'F01_Adult/t2/Adult_F01_31102012/mge_6/anatomy/F01_31102012_MGE_TEsum_magn.nii.gz'],
     [0,'F01_Adult/t2/Adult_F01_31102012/msme_11/anatomy/F01_31102012_MSME_TEsum_magn.nii.gz'],
     [3,'F17_P32/t2/P32_F17_06062014/AnalysisData/anatomy/P32_F17_06062014_MGE_TEsum_magn.nii.gz'],
     [3,'F17_P32/t2/P32_F17_06062014/AnalysisData/anatomy/P32_F17_06062014_MSME_TEsum_magn.nii.gz'],
     [3,'F17_P32/t2/P32_F17_06062014/RecoData/anatomy_msme_6/P32_F17_06062014_MSME_TEsum_magn.nii.gz'],
     [3,'F17_P32/t2/P32_F17_06062014/RecoData/anatomy_mge_5/P32_F17_06062014_MGE_TEsum_magn.nii.gz'],
     [1,'F25_P2/t2/P2_F25_31012015/anatomy/P2_F25_31012015_MSME_TEsum_magn.nii.gz'],
     [1,'F25_P2/t2/P2_F25_31012015/anatomy/P2_F25_31012015_MGE_TEsum_magn.nii.gz'],
     [3,'F21_P16/t2/P16_F21_01082014/anatomy/P16_F21_01082014_MGE_TEsum_magn.nii.gz'],
     [3,'F21_P16/t2/P16_F21_01082014/anatomy/P16_F21_01082014_MSME_TEsum_magn.nii.gz'],
     [1,'F22_Adult/t2/P64_F22/AnalysisData/anatomy/P64_F22_29082014_MGE5_TEsum_magn.nii.gz'],
     [3,'F22_Adult/t2/P64_F22/AnalysisData/anatomy/P64_F22_29082014_MGE13_TEsum_magn.nii.gz'],
     [3,'F22_Adult/t2/P64_F22/AnalysisData/anatomy/P64_F22_29082014_MSME_TEsum_magn.nii.gz'],
     [1,'F22_Adult/t2/P64_F22/RecoData/anatomy_mge_5/P64_F22_29082014_MGE_TEsum_magn.nii.gz'],
     [3,'F22_Adult/t2/P64_F22/RecoData/anatomy_mge_13/P64_F22_29082014_MGE_TEsum_magn.nii.gz'],
     [3,'F22_Adult/t2/P64_F22/RecoData/anatomy_msme_12/P64_F22_29082014_MSME_TEsum_magn.nii.gz']
]
dir='/pasteur/projets/cinq/rto/data/ferret/raw-data/'

rot0=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]); # OK
rot1=np.array([[0,1,0,0],[-1,0,0,0],[0,0,-1,0],[0,0,0,1]]); # OK
rot2=np.array([[0,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]]); # OK
rot3=np.array([[0,-1,0,0],[1,0,0,0],[0,0,-1,0],[0,0,0,1]]); # OK
rot4=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]); # OK

print("rot0: "+str(np.linalg.det(rot0)))
print("rot1: "+str(np.linalg.det(rot1)))
print("rot2: "+str(np.linalg.det(rot2)))
print("rot3: "+str(np.linalg.det(rot3)))
print("rot4: "+str(np.linalg.det(rot4)))

for r in sub:
    g=r[0];
    src=r[1]
    print(src);
    dst=src.split('/')[-1].split('.')[:-2][0] + '_rot.nii.gz';
    if g==0:
        rotate(dir+src,dir+'/'.join(src.split('/')[:-1])+'/'+dst,rot0);
    elif g==1:
        rotate(dir+src,dir+'/'.join(src.split('/')[:-1])+'/'+dst,rot1);
    elif g==2:
        rotate(dir+src,dir+'/'.join(src.split('/')[:-1])+'/'+dst,rot2);
    elif g==3:
        rotate(dir+src,dir+'/'.join(src.split('/')[:-1])+'/'+dst,rot3);
    elif g==4:
        rotate(dir+src,dir+'/'.join(src.split('/')[:-1])+'/'+dst,rot4);

