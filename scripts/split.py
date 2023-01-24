#/usr/bin/env python3
import os, shutil
import random
from os.path import isfile,join
from os import listdir, path
from random import sample
import glob

path = "/home/leo/yolo_ws/yolov5/datasets/face_lp_dataset/"
#list = [f for f in listdir(str(path)) if f.endswith('.jpg')]
lst = glob.glob(path + '*.jpg')
#print(list) 
random_list = sample(lst,15480)         #random_list'te pathli olarak jpgler var


try:
    os.mkdir('/home/leo/yolo_ws/yolov5/datasets/train/')
    
except FileExistsError:
    print('>>file already exist')

for item in random_list:

    name = item.split('/')[-1]      #name'de forex: (frame001.jpg) tutuluyor
    print(name)
    shutil.copy(item, '/home/leo/yolo_ws/yolov5/datasets/train/' + name)
    
    name1 = item.split('/')[-1]        #name1'de forex: (frame001.jpg) tutuluyor
    name1=  name1.rstrip("jpg")
    name1 = name1 + "txt"               # name1'de forex: (frame001.txt) tutuluyor.

    path1 = item.rstrip("jpg")          # fonksiyonun icine yazdigimiz(jpg) kismi atar 
    path1 = path1 + "txt"
    shutil.copy(path1, '/home/leo/yolo_ws/yolov5/datasets/train/' + name1)


