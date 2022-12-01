# -*- coding: utf-8 -*-
##Imports##
import streamlit as st 
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt 
import librosa
import librosa.display
import time
#import pandas as pd 
import numpy as np




##plots dos dados##
def plotfrequencydata():
    y = np.loadtxt("test.csv", delimiter = ',')
    data = np.abs(librosa.stft(y, n_fft = FRAME_SIZE, hop_length= HOP_SIZE))
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(data, ref=np.max), sr=sr, hop_length=HOP_SIZE, x_axis= "time", y_axis ='log')
    ax.set(title = "Power spectrogram")
    fig.colorbar(img, ax=ax,format= "%+2.f dB")
    graph1.pyplot(fig)
    
def plottimedata():
    y = np.loadtxt("test.csv", delimiter = ',')
    fig, ax = plt.subplots()
    img1 = librosa.display.waveshow(y)
    ax.set(title = "Sonogram")
    graph2.pyplot(fig)
    


##Fazer refresh da página de 5 em 5s)
#st_autorefresh(interval = 5000)

#Variáveis#
MQTT_broker = 'mqtt.eclipseprojects.io'
FRAME_SIZE = 512
HOP_SIZE = 128
sr = 22050


##Início do site##
header = st.container()
subheader = st.container()
header.title("IoT Sound Recorder")
subheader = st.subheader("Author: Dania Furk, Subject: AAIB")

##Botão para começar aquisição##
start_button, save_button = st.columns(2)
##Container para o gráfico##
graph1 = st.container()
graph2 = st.container()

if start_button.button("Start Recording"):
   client = mqtt.Client("Comando_gravar")
   client.connect(MQTT_broker)
   client.publish("daniafurkaaib/start", payload = "start")
   with st.spinner('Recording and Extracting Features'):
       time.sleep(13)
       plotfrequencydata()
       plottimedata()
       with open("test.csv", "rb") as file:
           save_button.download_button(
           label ="Download Data⬇️",
           data = file,
           file_name="data.csv",
           mime = "text/csv"
           )
    
    
    
    
        
       
       
           


       



   





   
   
   
   
    

