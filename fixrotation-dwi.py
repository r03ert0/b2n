import nibabel as nib
import numpy as np

def rotate(src,dst,rot):
    img=nib.load(src)
    print("orig:"+str(np.linalg.det(img.affine)))
    img.affine[:]=rot.dot(img.affine)
    nib.nifti1.save(img,dst)

sub=[
[3,'F01_Adult/dti/nii/F01_Adult.nii.gz'],
[2,'F02_P0/dti/nii/F02_P0.nii.gz'],
[2,'F03_Adult/dti/nii/F03_Adult.nii.gz'],
[2,'F04_Adult/dti/nii/F04_Adult.nii.gz'],
[1,'F05_Adult/dti/nii/F05_Adult.nii.gz'],
[1,'F06_P4/dti/nii/F06_P4.nii.gz'],
[1,'F07_P4/dti/nii/F07_P4.nii.gz'],
[1,'F08_P4/dti/nii/F08_P4.nii.gz'],
[2,'F10_P8/dti/nii/F10_P8.nii.gz'],
[2,'F16_P32/dti/nii/F16_P32.nii.gz'],
[1,'F17_P32/dti/nii/F17_P32.nii.gz'],
[4,'F19_P32/dti/nii/F19_P32.nii.gz'],
[3,'F20_P16/dti/nii/F20_P16.nii.gz'],
[1,'F21_P16/dti/nii/F21_P16.nii.gz'],
[2,'F22_Adult/dti/nii/F22_Adult.nii.gz'],
[2,'F25_P2/dti/nii/F25_P2.nii.gz'],
[1,'F28_P2/dti/nii/F28_P2.nii.gz']
]
dir='/pasteur/projets/cinq/rto/data/ferret/raw-data/'

rot1=np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]); # OK
rot2=np.array([[0,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]]); # OK
rot3=np.array([[0,-1,0,0],[1,0,0,0],[0,0,-1,0],[0,0,0,1]]); # OK
rot4=np.array([[0,1,0,0],[-1,0,0,0],[0,0,-1,0],[0,0,0,1]]); # OK

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

