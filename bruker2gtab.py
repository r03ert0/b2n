####### Extract bval and bvec files from the corresponding method file #######

### V1, 03.05.2016, Celine ###
### V2, 08.08.2017, Roberto ### add output path

import re #regular expression
from pandas import DataFrame
import numpy as np
import fire

def getBvals(bruker_path, out_path):
    """
    Extract bvals from 'method' file in a data frame
    """
    f = open(bruker_path+'/method',"r")
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
            bval.to_csv(out_path+'/bvals', sep=" ", index=False, header=False) #save data frame in a file 
    f.close()
    

def getBvecs(bruker_path, out_path):
    """
    Extract bvecs from 'method' file in a data frame
    """
    
    f = open(bruker_path+'/method',"r")

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
    bvecs.to_csv(out_path+'/bvecs', sep=" ", index=False, header=False) #save data frame in a file 
    
def getInfo(bruker_path, out_path):
    """
    Get info
    PVM_Matrix= ==>x, y
    PVM_SPackArrNSlices= ==>z
    PVM_SpatResol= ==> resolution in x, y
    PVM_SPackArrSliceDistance= ==> resolution in z
    nb bval
    """
    f = open(bruker_path+'/method',"r")

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

    info = DataFrame(info_arr)
    info.to_csv(out_path+'/info.csv', sep=" ", index=False, header=False) #save data frame in a file

def main():
    fire.Fire();
if __name__ == '__main__':
    main()


