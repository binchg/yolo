# -*-coding: UTF-8 -*-
import logging
import os
import tarfile


def merge(tarPath):
    cmd = r'cat {}.* > {}'.format(tarPath, tarPath)
    print("merge")
    logging.warning('merge')
    os.system(cmd)  # 调用cmd解压


def un_tar(file_name):
    # untar zip file"""
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    # 因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()

def extract(tar_path, target_path):
    try:
        tar = tarfile.open(tar_path, "r:gz")
        file_names = tar.getnames()
        for file_name in file_names:
            tar.extract(file_name, target_path)
        tar.close()
    except Exception as e:
        raise Exception(e)


def tarUpzip(tarPath, targetPath):
    cmd = r'tar -jxv -f  {}  {}'.format(tarPath, targetPath)
    print("tarpzip")
    os.system(cmd)  # 调用cmd解压


if __name__ == '__main__':
    merge("/content/drive/MyDrive/yolo/FLIR_ADAS_1_3.tar")
    print("ok")
    logging.warning('ok')
