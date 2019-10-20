#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gmplot 
import webbrowser
import time
from selenium import webdriver
from gtts import gTTS
from pygame import mixer
def trigger_heatmap(msg):
    try:
        driver.close()
    except:
        pass
    #kiit square must be potrayed in map
    latitude_list = [20.4093164, 20.1924519, 20.4093164,20.1924519 ] 
    longitude_list = [ 85.9028721, 85.7380342, 85.9028721,85.7380342 ] 
    gmap = gmplot.GoogleMapPlotter(20.3548,85.8153, 15) 
    lat=[msg[0]]
    lon=[msg[1]]      
    gmap.heatmap(lat,lon)
    #gmap.circle(lat,lon, radius=50 ,color='red')
    
    
    gmap.draw( "map11.html" )     
    driver = webdriver.Chrome("chromedriver.exe")
    url = "map11.html"
    driver.get(url)
def play_siren():
    name="nuclear_alarm.mp3"
    mixer.init()
    mixer.music.load(name)
    mixer.music.play()


# In[ ]:


import socket
import time
import pickle
import webbrowser
import time
from selenium import webdriver

Violent_mappings=[]

IP = "127.0.0.1"
PORT = 12345

#creating a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


#server binding to a port no and ip
server_socket.bind((IP,PORT))

#can take upto 50 requests in queue
server_socket.listen(50)
while True:
    print(Violent_mappings)
    flag1=0
    flag2=0
    client_socket, client_address = server_socket.accept()
    msg=client_socket.recv(1024)
    msg=pickle.loads(msg)
    #print(msg)
    if msg[2]=="V":
        for x in Violent_mappings:
            if x==msg:
                flag1=1
        if flag1==0:
            Violent_mappings.append(msg)
            trigger_heatmap(msg)
            play_siren()
        else:
            pass
    elif msg[2]=="NV":
        for x in Violent_mappings:
            if x[0]==msg[0] and x[1]==msg[1]:
                msg[2]="V"
                flag2=1
        if flag2==1:
            Violent_mappings.remove(msg)
            try:
                driver.close()
            except:
                pass
        else:
            pass
   


# In[ ]:





# In[ ]:





# In[ ]:




