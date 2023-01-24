import sys
import argparse

from tqdm import tqdm

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*500))    # added this line 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        # print(type(image))
        # cv2.imshow("image", image)
        cv2.imwrite( pathOut + "frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
