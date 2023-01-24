import os
import time
from os import listdir, rename
from os.path import isfile, join
ext = 'txt'

folder_path = "./etiketlenecek"
filenames = sorted([f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f[-3:] == ext])

for f in filenames:
    f2 = open(folder_path+"/"+f, 'r')
    txt=1
    #print("\n"+"Dosya adi = "+f+"\n")
    if(txt):
        txt=f2.read()
        """print(txt)
        print('str = '+str(len(str(txt))))"""
        if len(str(txt))<1:
            oldFileName = folder_path+'/'+f
            f1=f.rsplit("."+ext)
            newfilename = folder_path+'/'+f1[0]+'*'
            print(newfilename)
    f2.close()
