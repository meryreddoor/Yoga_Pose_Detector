import json
from keras.models import load_model
from keras.models import model_from_json
import cv2 
import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def prediction_pose(path):
    ''' Recognice the food in a given image ''' 

    # loading the model 
    model_json = open('../modelos/model_json.json', 'r')
    loaded_model = model_json.read()
    model_json.close()
    model = model_from_json(loaded_model)
    model.load_weights("../modelos/model_h5.h5")

    # image preprocessing - pasarlo a DF, cambiarle el color y el tamaño
    
    dictionary = {}
    for paths in glob.glob(path):
        dictionary.setdefault('pose', []).append(paths.split('/')[-2])
        dictionary.setdefault('png', []).append(paths.split('/')[-1])
        dictionary.setdefault('path', []).append(paths)
        dictionary.setdefault('array', []).append(cv2.resize(cv2.imread(paths, cv2.IMREAD_GRAYSCALE),(224,224)))
    images = pd.DataFrame(dictionary)
    
    data_ima = images

    outsider_img = np.stack(data_ima['array'])
    outsider_img = outsider_img / 255

    # predict

    pic = outsider_img # transform pic
    plt.subplot(122)
    plt.imshow(Image.fromarray(pic.squeeze()*255)) # transformed pic
    pic = np.expand_dims(pic,axis=0).reshape(np.expand_dims(pic,axis=0).shape[0], 224, 224, 1)
    pred = model.predict(pic)[0]
    print('OUTSIDER')
    print('')
    print("Probabilidades totales -> ardha matsyendrasana:{0:.5f} bakasana:{1:.5f} bitilasana:{2:.5f} chaturanga dandasana:{3:.5f} garudasana:{4:.5f} vriksasana:{5:.5f}".format(pred[0],pred[1],pred[2],pred[3],pred[4],pred[5]))
    print('')
    #clases = ['ardha matsyendrasana','bakasana','bitilasana','chaturanga dandasana','garudasana','vriksasana']
    #print(f'Probability: {max(pred)}--> {clases[np.argmax(pred)]}')
    return