### V1, 03.05.2016, Celine ###
####### Extract bval and bvec files from the corresponding method file #######

import re #regular expression
from pandas import DataFrame
import numpy as np
import fire

def getBvals(path):
    """
    Extract bvals from 'method' file in a data frame
    """
    f = open(path+'/method',"r")
    for line in f:
        if re.search(r'PVM_DwEffBval=',line): #find parameter of bval
            #print line
            ne = f.next() #read line after the name of the parameter
            nb_str = ne.split()
            bval_arr = [float(x) for x in nb_str] #first line in an array
            ne = f.next()
            while(re.match("[-+]?\d*\.\d+|\d+",ne)!=None): #while the next line is made of floats parse in the array
                nb_str2 = ne.split()
                for x in nb_str2:
                    bval_arr.append(x)
                ne = f.next()
            bval = DataFrame(bval_arr) #array in data frame
            bval=bval.transpose() #transpose data frame to have one line with all the bvals
            bval.to_csv(path+'/bvals', sep=" ", index=False, header=False) #save data frame in a file 
    f.close()
    

def getBvecs(path):
    """
    Extract bvecs from 'method' file in a data frame
    """
    
    f = open(path+'/method',"r")

    for line in f:
        if re.search(r'PVM_DwAoImages=',line):
            nb0=line.split('=')[1]
            nb0=int(nb0)
	if re.search(r'PVM_DwDir=',line): #find parameter of bvec
            #print line
            p=re.compile('(\d+)');
            dim=[int(x) for x in p.findall(line)]
            bvecs_arr = np.zeros((dim[1],dim[0]+nb0)) #define the bvec array (3 lines (x,y,z), same number as bval columns)
            i=0
            ne = f.next() #read line after the name of the parameter
            while(re.match("[-+]?\d*\.\d+|\d+",ne)!=None): #while the next line is made of floats parse in the array
                nb_str = ne.split()
                for x in nb_str:
                    j = i%3 #line number (modulo)
                    k = i/3 #column number
                    bvecs_arr[j][k+nb0] = float(x) #assign value in the array (+nb0 because nb0 first B0 are 0)
                    i=i+1
                ne = f.next() #when all floats of the current line are done, go to the next
    f.close()
    bvecs = DataFrame(bvecs_arr) #array in data frame
    bvecs.to_csv(path+'/bvecs', sep=" ", index=False, header=False) #save data frame in a file 
    
def getInfo(path):
    """
    Get info
    PVM_Matrix= ==>x, y
    PVM_SPackArrNSlices= ==>z
    PVM_SpatResol= ==> resolution in x, y
    PVM_SPackArrSliceDistance= ==> resolution in z
    nb bval
    """
    f = open(path+'/method',"r")

    for line in f:
        if re.search(r'PVM_DwNDiffExp=',line):
            nvols=int(line.split('=')[1])
        if re.search(r'PVM_Matrix=',line): 
            ne = f.next()
            nb_str = ne.split()
            mat_x = int(nb_str[1])
            mat_y = int(nb_str[0])
        if re.search(r'PVM_SPackArrNSlices=',line):
            ne = f.next()
            mat_z = int(ne)
        if re.search(r'PVM_SpatResol=',line):
            ne = f.next()
            nb_str = ne.split()
            res_x = float(nb_str[1])
            res_y = float(nb_str[0])
        if re.search(r'PVM_SPackArrSliceDistance=',line):
            ne = f.next()
            res_z = float(ne)
    f.close()

    info_arr = np.zeros((3,3))
    info_arr[0][0] = mat_x
    info_arr[0][1] = mat_y
    info_arr[0][2] = mat_z
    info_arr[1][0] = mat_x * res_x
    info_arr[1][1] = mat_y * res_y
    info_arr[1][2] = mat_z * res_z
    info_arr[2][0] = nvols

    #print info_arr
    info = DataFrame(info_arr)
    info.to_csv(path+'/info.txt', sep=" ", index=False, header=False) #save data frame in a file

# Replace with your parameters, rest doesnt need changes #
srcDir='/pasteur/projets/policy01/cinq/rto/data/ferret/raw-data/'
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
#    getBvals(srcDir+s[0]+s[1])
#    getBvecs(srcDir+s[0]+s[1])
#    getInfo(srcDir+s[0]+s[1])

def main():
    fire.Fire();
if __name__ == '__main__':
    main()


