import tensorflow as tf
import h5py
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import models
from keras.models import Model
from keras import initializers
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" #remove the warning of the tensorflow
import argparse

#goodnet
class GoodNet(Model):
    def __init__(self, bd_model, bd_model_pruned):
        super(GoodNet, self).__init__()
        self.bd_model = bd_model
        self.bd_model_pruned = bd_model_pruned
    
    def predict(self, x):
        bd_model_pred = np.argmax(self.bd_model.predict(x), axis=1)
        bd_model_pruned_pred = np.argmax(self.bd_model_pruned.predict(x), axis=1)
        pred = np.zeros(len(bd_model_pred))
        pred[np.where(bd_model_pred==bd_model_pruned_pred)]=bd_model_pred[np.where(bd_model_pred==bd_model_pruned_pred)]
        pred[np.where(bd_model_pred!=bd_model_pruned_pred)]=int(1283)
        return pred
        
def reference(img_path, bd_model_path, pruned_model_path):
    bd_model = keras.models.load_model(bd_model_path)
    pruned_model = keras.models.load_model(pruned_model_path)
    gd_model = GoodNet(bd_model, pruned_model)
    img = np.expand_dims(np.array(Image.open(img_path))/255,axis=0)
    result = gd_model.predict(img)
    return result
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', type=str, default='/content/test.jpg')
    parser.add_argument('--bd_model_path', type=str, default='/content/ML_Cyber_Project_2021/bd_model/multi_trigger_multi_target_bd_net.h5')
    parser.add_argument('--pruned_model_path', type=str, default='/content/ML_Cyber_Project_2021/fine_pruned_model/multi_trigger_multi_target_bd_model_pruned.h5')
    opt = parser.parse_args()
    print(int(reference(**vars(opt))))