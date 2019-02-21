from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import numpy as np
import os
from PIL import Image
import cv2
import keras
#load json and create model
def load_model():
    json_file = open('model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    #load weights into new model
    loaded_model.load_weights("model/model.h5")
    #print("loaded model from disk")

    #Evaluate on test data
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', 
                      metrics=['accuracy'])
    return loaded_model

def convert_to_array(img):
    im = cv2.imread(img)
    img = Image.fromarray(im, 'RGB')
    image = img.resize((50, 50))
    return np.array(image)

def get_shot_name(label):
    if label==0:
        return "transitioning"
    if label==1:
        return "close_up"
    if label==2:
        return "zoom_in"
    if label==3:
        return "long_shot"


def predict_shot(file,new_model):
    #print("Predicting .................................")
    loaded_model = new_model
    ar=convert_to_array(file)
    ar=ar/255
    label=1
    a=[]
    a.append(ar)
    a=np.array(a)
    score=loaded_model.predict(a,verbose=1)
    #print(score)
    label_index=np.argmax(score)
    #print(label_index)
    acc=np.max(score)
    shot=get_shot_name(label_index)
    return(shot)
    #print(shot)
    #print("The predicted shot is a "+shot+" with accuracy =    "+str(acc))

#predict_shot("model/longtest.jpg")

def analysisShot():
    folder_num = 0

    shot_arr = []

    path = 'frames'

    new_model = load_model()

    #Find the number of folders availible
    for path, dirs, files in os.walk(path):
        folder_num += len(dirs)

    for i in range(0, folder_num):
       # print("Goes through " +str(i))
        shot_arr.append(predict_shot('frames/'+str(i)+'/0.jpg', new_model))
        

    return(shot_arr)

analysisShot()