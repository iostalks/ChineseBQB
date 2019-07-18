# -*- coding: utf-8 -*-

import os
import shutil

# 移动文件
def move_file(srcPath, dstPath):
    tmpFiles = os.listdir(srcPath)
    for file in tmpFiles:
        if (file == '.DS_Store'):
            continue
        src = os.path.join(tmpFilePath, file);
        shutil.move(src, dstPath)

# 获取图片所在文件夹名称
path = os.getcwd()
slashIndex = path.rfind("/")
dirName = path[slashIndex+4:]

# 创建临时文件夹
tmpFilePath = path + '/tmp/'
folder = os.path.exists(tmpFilePath)
if not folder:
    os.makedirs(tmpFilePath)
    print("tmp 文件夹已创建")
else:
    print("tmp 文件夹已存在")

# 遍历文件修改名字
files= os.listdir(path)

j = 0
for i in range(len(files)):
    imgName = files[i]
    if (imgName == '.DS_Store' or imgName == 'rename.py' or imgName == 'tmp'):
        continue;
    pointIndex = imgName.find('.')
    postfix = imgName[pointIndex:]

    f_src = os.path.join(path, imgName);
    os.rename(path + "/" + imgName, tmpFilePath + dirName + ("%03d" % j) + postfix)
    j += 1;

move_file(tmpFilePath, path)
os.rmdir(tmpFilePath)


print("修改完成")
