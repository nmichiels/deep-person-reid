from __future__ import division, print_function, absolute_import
import re
import glob
import os.path as osp
import warnings

from ..dataset import VideoDataset
import numpy as np

class DroneDataset(VideoDataset):
    """DroneDataset.
    """
    dataset_dir = 'drone_dataset'


    def __init__(self, root='', **kwargs):
        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)
        print("debug:",self.dataset_dir)
        
        path = glob.glob(self.dataset_dir)[0]
        

        
        # from numpy import genfromtxt

        # my_data = genfromtxt(self.dataset_dir + '/data.csv', delimiter=',')

        data = np.loadtxt(self.dataset_dir + '/data2.csv', dtype=np.int32, delimiter=';', skiprows=1)
        
        currentPid = 0
        currentCamId = 0
        tracklets = []
        img_paths = []
        for i in range(0, data.shape[0]):
            pid = data[i,2]
            camid = data[i,1]
            img_path = path + '/' + 'view%d/'%camid + str(data[i,0]) + ".jpg"
            
            
            if pid == currentPid:
                img_paths.append(img_path)
            else:
                tracklets.append((img_paths, currentPid, currentCamId))
                img_paths = []
                img_paths.append(img_path)
                currentCamId = camid
                currentPid = pid
                
              

        
        train = tracklets#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])]
        query = tracklets#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, 1)]
        gallery = tracklets#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])]

        # train = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])])
        # query = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0]])])
        # gallery = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])])
        

       

        super(DroneDataset, self).__init__(train, query, gallery, **kwargs)

