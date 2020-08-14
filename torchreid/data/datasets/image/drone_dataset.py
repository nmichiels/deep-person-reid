from __future__ import division, print_function, absolute_import
import re
import glob
import os.path as osp
import warnings

from ..dataset import ImageDataset
import numpy as np

class DroneDataset(ImageDataset):
    """DroneDataset.
    """
    dataset_dir = 'drone_dataset'


    def __init__(self, root='', **kwargs):
        self.root = osp.abspath(osp.expanduser(root))
        self.dataset_dir = osp.join(self.root, self.dataset_dir)
        
        
        path = glob.glob(self.dataset_dir)[0]
        

        
        # from numpy import genfromtxt

        # my_data = genfromtxt(self.dataset_dir + '/data.csv', delimiter=',')

        data = np.loadtxt(self.dataset_dir + '/data2.csv', dtype=np.int32, delimiter=';', skiprows=1)
        
        
        #first element
        prev_pid = data[0,2]
        prev_camid = data[0,1]
        img_path = path + '/' + 'view%d/'%prev_camid + str(data[0,0]) + ".jpg"
        
        current_camid = prev_camid
        current_pid = prev_pid
        images = []
        images.append((img_path, current_pid, current_camid))
        

            
            
        for i in range(1, data.shape[0]):
            pid = data[i,2]
            camid = data[i,1]
            img_path = path + '/' + 'view%d/'%camid + str(data[i,0]) + ".jpg"
            
            
            if pid == prev_pid and camid == prev_camid:
                # current_camid += 1
                # images.append((img_path, pid, current_camid))
                
                prev_pid = pid
                prev_camid = camid
                
            else:
                current_camid += 1
                current_pid += 1
                images.append((img_path, 0, camid))#current_camid))
                print( pid, current_camid)
                # current_camid = camid
                prev_pid = pid
                prev_camid = camid
              
              
          # #first element
        # img_path = path + '/' + str(data[0,0]) + ".jpg"
        # prev_pid = data[0,2]
        # prev_camid = data[0,1]
        # current_camid = prev_camid
        # images = []
        # images.append((img_path, prev_pid, prev_camid))
        
              
        # for i in range(1, data.shape[0]):
            # img_path = path + '/' + str(data[i,0]) + ".jpg"
            # pid = data[i,2]
            # camid = data[i,1]
            
            # if pid == prev_pid and camid == prev_camid:
                # current_camid += 1
                # images.append((img_path, pid, current_camid))
                
                # prev_pid = pid
                # prev_camid = camid
                
            # else:
                # images.append((img_path, pid, camid))
                # current_camid = camid
                # prev_pid = pid
                # prev_camid = camid
              
              
              

        
        train = images#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])]
        query = images#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, 1)]
        gallery = images#[(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])]

        # train = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])])
        # query = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0]])])
        # gallery = ([(path + '/' + str(data[i,0]) + ".jpg", data[i,2], data[i,1]) for i in range(0, data.shape[0])])
        

       

        super(DroneDataset, self).__init__(train, query, gallery, **kwargs)

