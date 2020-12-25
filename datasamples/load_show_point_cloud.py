# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 1:53
# @Author  : BIPLab SCUT
# @File    : 
# @Software: PyCharm
import struct
from pathlib import Path
import numpy as np
import inspect
import re
import torch
import pandas as pd
import cv2
import time



def load_point_cloud(sub, t, data_dir):
    '''
    导入点云文件（pts自定义格式）
    :param sub:  subject编号
    :param t:  采样次
    :param data_dir: 数据集目录
    :return: point_cloud: [400, 400, 4]
    '''
    
    sample_name = '{}-{}.pts'.format(sub, t)
    sample_path = Path(data_dir).joinpath(sample_name)
    if not sample_path.exists():
        raise RuntimeError('{} does not exists.'.format(sample_path))

    f = sample_path.open('rb')
    data = f.read(4)
    num_points = struct.unpack('i', data)[0]
    data = f.read(4)
    num_ellipses = struct.unpack('i', data)[0]
    point_cloud = np.zeros((num_points, num_ellipses, 4))
    for i in range(num_points):
        for j in range(num_ellipses):
            x = f.read(4)
            x = struct.unpack('f', x)[0]
            point_cloud[i, j, 0] = x

    for i in range(num_points):
        for j in range(num_ellipses):
            y = f.read(4)
            y = struct.unpack('f', y)[0]
            point_cloud[i, j, 1] = y

    for i in range(num_points):
        for j in range(num_ellipses):
            z = f.read(4)
            z = struct.unpack('f', z)[0]
            point_cloud[i, j, 2] = z

    for i in range(num_points):
        for j in range(num_ellipses):
            g = f.read(4)
            g = struct.unpack('f', g)[0]
            point_cloud[i, j, 3] = g

    f.close()

    return point_cloud
    
def visualize(point_cloud):
    '''
    调用mayavi库可视化3D指静脉点云
    :param point_cloud: 点云，[400, 400, 4]
    :return:
    '''
    x = point_cloud[:, :, 0]
    y = point_cloud[:, :, 1]
    z = point_cloud[:, :, 2]
    g = point_cloud[:, :, 3]

    from mayavi import mlab

    fig1 = mlab.figure(bgcolor=(0, 0, 0), size=(800, 600))
    # mlab.points3d(x, y, z, g, mode='point', colormap='spectral', color=(1, 0, 0), figure=fig1)
    mlab.points3d(x, y, z, g, mode='point', colormap='spectral', figure=fig1)
    mlab.show()
    
def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)
    
if __name__ == '__main__':
    dataset_dir = 'H:\实验室给我的资料\Javad_Khodadoust_manuscript\code\To-Javad\part of 3D finger-vein dataset\Point Cloud with texture for 3D finger-vein models'
    point_cloud = load_point_cloud(1, 6, dataset_dir)
    print('point_cloud: {}'.format(point_cloud.shape))
    visualize(point_cloud)
    # print(varname(point_cloud))