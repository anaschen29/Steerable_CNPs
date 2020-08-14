#LIBRARIES:
#Tensors:
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as utils

#E(2)-steerable CNNs - librar"y:
from e2cnn import gspaces                                          
from e2cnn import nn as G_CNN   
#import e2cnn

#Plotting in 2d/3d:
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
from matplotlib.colors import Normalize
import matplotlib.cm as cm

#Tools:
import datetime
import sys
import os 

sys.path.append("./")

#Own files:
import Kernel_and_GP_tools as GP
import Tasks.GP_Dataset as MyDataset

#A function to load the GP data which I sampled:
def load_GP_div_free(data_set='train',path_to_folder='Tasks/GP_div_free_small/'):
    #Load the data:
    if data_set=='test':
        X=np.load(path_to_folder+"Data/GP_Small_Test_X.npy")
        Y=np.load(path_to_folder+"Data/GP_Small_Test_Y.npy")
    elif data_set=='train':
        X=np.load(path_to_folder+"Data/GP_Small_Train_X.npy")
        Y=np.load(path_to_folder+"Data/GP_Small_Train_Y.npy")
    elif data_set=='valid':
        X=np.load(path_to_folder+"Data/GP_Small_Valid_X.npy")
        Y=np.load(path_to_folder+"Data/GP_Small_Valid_Y.npy")
    else:
        sys.exit('Unkown data set type. Must be either train, valid or test')

    X=torch.tensor(X,dtype=torch.get_default_dtype())
    Y=torch.tensor(Y,dtype=torch.get_default_dtype())

    return(X,Y)

def give_GP_div_free_data_set(Min_n_cont,Max_n_cont,n_total,data_set='train',path_to_folder='Tasks/GP_div_free_small/'):
    X,Y=load_GP_div_free(data_set=data_set,path_to_folder=path_to_folder)
    return(MyDataset.CNPDataset(X,Y,Min_n_cont=Min_n_cont,Max_n_cont=Max_n_cont,n_total=n_total))
