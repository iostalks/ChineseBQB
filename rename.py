# -*- coding: utf-8 -*-

import os
import sys
import shutil
from map_gif import img_formate_to_gif

# 移动文件
def move_file(srcPath, dstPath):
    tmpFiles = os.listdir(srcPath)
    for file in tmpFiles:
        if (file == '.DS_Store'):
            continue
        src = os.path.join(srcPath, file);
        shutil.move(src, dstPath)

img_formate_to_gif()

# 表情文件夹名称
imgs_dir_name = sys.argv[1]

# 表情文件夹路径
imgs_dir_path = os.path.join(os.getcwd(), imgs_dir_name)
print(imgs_dir_path)

# 创建临时文件夹
imgs_tmp_dir_path = os.path.join(imgs_dir_path, 'tmp')

has_tmp_dir = os.path.exists(imgs_tmp_dir_path)
if not has_tmp_dir:
    os.makedirs(imgs_tmp_dir_path)

imgs_path_files = os.listdir(imgs_dir_path)

j = 0
for i in range(len(imgs_path_files)):
    file_name = imgs_path_files[i]
    if file_name == 'index.md':
        os.remove(os.path.join(imgs_dir_path, 'index.md'))
    if (file_name == '.DS_Store' or file_name == 'rename.py' or file_name == 'tmp'):
        continue;
    point_index = file_name.find('.') # 取后缀名
    suffix = file_name[point_index:] # 后缀名
    print(suffix)

    img_src_path = os.path.join(imgs_dir_path, file_name);
    img_dst_path = os.path.join(imgs_tmp_dir_path, imgs_dir_name[3:] + ("%03d" % j) + suffix)
    print(img_src_path, img_dst_path)
    os.rename(img_src_path, img_dst_path)
    j += 1;

move_file(imgs_tmp_dir_path, imgs_dir_path)
os.rmdir(imgs_tmp_dir_path)

print("修改完成")
