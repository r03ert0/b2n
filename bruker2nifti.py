import os
import nibabel as nib
import numpy as np
import fire

def convertBrukerToNifti1(input_dir,output_path):
    # parameter files
    method=input_dir+'/method'
    acqp=input_dir+'/acqp'
    pdata=input_dir+'/pdata'

    # parse number of volumes and slice thickness
    f = open(method, 'r')
    x = f.readlines()
    f.close()
    for i in x:
        a=i.split('=');
        if(a[0]=='##$PVM_DwNDiffExp'):
            nvols=int(a[1])
        if(a[0]=='##$PVM_DwUsedSliceThick'):
            thz=float(a[1])

    # parse number of slices
    f = open(acqp, 'r')
    x = f.readlines()
    f.close()
    for i in x:
        a=i.split('=');
        if(a[0]=='##$NSLICES'):
            dimz=int(a[1])

    # parse data type, slice dimensions and FOV (used to compute pixel thickness)
    dd=os.listdir(pdata)
    for p in dd:
        reco=pdata+'/'+p+'/reco'
        if(os.path.isfile(reco)):

            # read binary data
            f=open(pdata+'/'+p+'/2dseq','r')
            img=f.read();
            f.close()

            # gather header info
            f = open(reco, 'r')
            x = f.readlines()
            f.close()
            state=0
            for i in x:
                a=i.split('=');
                if(a[0]=='##$RECO_wordtype'):
                    data_type=a[1].replace('\n','')
                    if(data_type=="_16BIT_SGN_INT"):
                        data_type="int16"
                        datatype=4;
                        bitpix=16;
                    else:
                        print "ERROR: Unknown data type "+data_type;
                if(state==1):
                    dimx=int(i.split(' ')[0])
                    dimy=int(i.split(' ')[1])
                    state=0
                if(state==2):
                    fovx=float(i.split(' ')[0])*10
                    fovy=float(i.split(' ')[1])*10
                    state=0
                if(a[0]=='##$RECO_inp_size'):
                    state=1
                if(a[0]=='##$RECO_fov'):
                    state=2        

    # convert binary data to array
    arr0=np.frombuffer(img,data_type);
    arr=arr0.reshape(dimy,dimx,dimz,nvols,order='F')
    arr=np.swapaxes(arr,0,1)
    arr=np.flip(arr,0)
    arr=np.flip(arr,1)

    # make a new nifti1 volume
    affine=np.diag([1,1,1,1])
    nii=nib.nifti1.Nifti1Image(arr, affine)
    hdr=nii.header

    hdr['dim']=[4,dimx,dimy,dimz,nvols,1,1,1]
    hdr['datatype']=datatype
    hdr['bitpix']=bitpix
    hdr['pixdim']=[0,fovx/dimx,fovy/dimy,thz,1,1,1,1]
    hdr['vox_offset']=352
    hdr['scl_slope']=1;
    hdr['scl_inter']=0;
    hdr['descrip']="Created with love"
    hdr['qform_code']=0
    hdr['sform_code']=1
    hdr['quatern_b']=0
    hdr['quatern_c']=0
    hdr['quatern_d']=0
    hdr['qoffset_x']=0
    hdr['qoffset_y']=0
    hdr['qoffset_z']=0
    hdr['srow_x']=[fovx/dimx,0,0,0]
    hdr['srow_y']=[0,fovy/dimy,0,0]
    hdr['srow_z']=[0,0,thz,0]
    hdr['magic']='n+1'

    nii.affine[:]=hdr.get_sform() # to get the transformation matrix into the image file

    # save
    nib.nifti1.save(nii,output_path)

print "bruker2nii.py"

srcDir='/pasteur/projets/policy01/cinq/rto/data/ferret/raw-data/'
dstDir='/pasteur/projets/policy01/cinq/rto/data/ferret/raw-data/'
sub=[
    ['F01_Adult','/dti/10'],
    ['F02_P0','/dti/0'],
    ['F03_Adult','/dti/9'],
    ['F04_Adult','/dti/8'],
    ['F05_Adult','/dti/0'],
    ['F06_P4','/dti/10'],
    ['F07_P4','/dti/7'],
    ['F08_P4','/dti/11'],
    ['F10_P8','/dti/7'],
    ['F16_P32','/dti/8'],
    ['F17_P32','/dti/7'],
    ['F19_P32','/dti/8'],
    ['F20_P16','/dti/9'],
    ['F21_P16','/dti/7'],
    ['F22_Adult','/dti/14'],
    ['F22_Adult','/dti/7'],
    ['F25_P2','/dti/7'],
    ['F28_P2','/dti/8']
];
#for s in sub:
#    print s[0];
#    convertBrukerToNifti1(srcDir+s[0]+s[1],dstDir+s[0]+'.nii.gz');

def main():
    fire.Fire(convertBrukerToNifti1);
if __name__ == '__main__':
  main()
