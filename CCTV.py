#!/usr/bin/env python
# coding: utf-8

# In[20]:


def detection_of_violent_activities(vid_seq):
    #reshaping the 10 frames as per the model
    test=[]
    test.append(vid_seq)
    inputtestshape=[]
    inputtestshape.append(test)
    
    #convert the list into an array
    inputtestshape=np.array(inputtestshape).reshape(-1,10,100,100,3)
    
    #predicting the probabilities of violent and non-violent activities
    prediction=violent_detector_model.predict_proba(inputtestshape)
    #calculation the maximum probability
    result=np.argmax(prediction)
    actions=["non-violent","violent"]
    return(result)
def sendtoserver(v):
    IP = "127.0.0.1"
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,PORT))
    lat=20.34901
    long=85.83627
    msg=[lat,long,v]
    print(msg)
    msg=pickle.dumps(msg)
    s.send(msg)
    s.close


# In[21]:


#import modules
import socket
import time
import pickle
import cv2
import numpy as np
import tensorflow as tf

#loading the violent detection model
violent_detector_model=tf.keras.models.load_model("violent_detector.h5")

#allocation of camera
vid_cap=cv2.VideoCapture("1.mpg")

#list that will later be used to store the frames in a sequence of 10
vid_seq=[]

while True:
    try:
        #extract each frame
        success,frames=vid_cap.read()
        #resize the frame to put it in model
        frames=cv2.resize(frames,(100,100))
        if(len(vid_seq)%10)==0 and len(vid_seq)!=0:
            #call a function for detection
            ret_value=detection_of_violent_activities(vid_seq)
            if ret_value==1:
                sendtoserver("V")
            elif ret_value==0:
                sendtoserver("NV")
            vid_seq=vid_seq[1:len(vid_seq)]
            pass
        else:
            vid_seq.append(frames)
            
    except:
        print("FRAMES NOT FOUND")
        break
    
    


# In[ ]:





# In[ ]:





# In[ ]:




