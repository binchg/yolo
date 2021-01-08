# -*- coding: utf-8 -*-
import time
import os
import shutil
import string


def readFilename(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            readFilename(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile

def buildFile(path1,path2):
    # 图片地址
    path1 = path1
    allfile1 = []
    allfile1 = readFilename(path1, allfile1)
    allname1 = []
    # 放入的txt文件
    txtpath = path2
    with open(txtpath, 'w') as fp:
        for name in allfile1:
            file_cls = name.split("/")[-1].split(".")[-1]
            if file_cls == 'jpeg':
                fp.write("".join(name) + "\n")

if __name__ == '__main__':
    path = "/Users/bytedance/gitlabclone/Object-Detection-on-Thermal-Images/coco/images/FLIR_Dataset/training/Data/"
    buildFile(path,path+"train/train.txt")
    # buildFile(path+"train/Annotated_thermal_8_bit",path+"train/train.txt")
