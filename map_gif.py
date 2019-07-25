# -*- coding: utf-8 -*-
import os
import sys

def img_formate_to_gif():
    curPath = os.getcwd()
    directory = sys.argv[1];
    dstPath = os.path.join(curPath, directory);
    files = os.listdir(dstPath)
    for filename in files:
        print(filename)
        portion = os.path.splitext(filename)
        if portion[1] == '.png' or portion[1] == '.jpg' or portion[1] == '.JPG':
            originFileName = os.path.join(dstPath, filename)
            newName = dstPath + '/' + portion[0] + '.gif'
            os.rename(originFileName, newName)
            print('modified', originFileName, newName)

# img_formate_to_gif()
