# -*- coding: utf-8 -*-
import os
import sys

def img_formate_to_gif():
    curPath = os.getcwd()
    directory = sys.argv[1];
    dstPath = os.path.join(curPath, directory);
    files = os.listdir(dstPath)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == '.png' or portion[1] == '.jpg':
            originFileName = os.path.join(dstPath, filename)
            newName = dstPath + '/' + portion[0] + '.gif'
            os.rename(originFileName, newName)
            print('modified', originFileName, newName)

def main():
    img_formate_to_gif()
    print('finished')


if __name__ == '__main__':
    main()
