# -*- coding: utf-8 -*-
##Imports##
import streamlit as st 
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt 
import librosa
import time
#import pandas as pd 
import numpy as np
from streamlit_autorefresh import st_autorefresh


##plots dos dados##
def plotdata():
    y = np.loadtxt("pmvalues.csv", delimiter = ',')
    times = librosa.times_like(y)
    fig, ax = plt.subplots()
    ax.semilogy(times, y, label='RMS Energy')
    graph.pyplot(fig)
    
##Fazer refresh da página de 5 em 5s)
#st_autorefresh(interval = 5000)

#Variáveis#
MQTT_broker = 'test.mosquitto.org'


##Início do site##
header = st.container()
header.title("Aquisição de som")
##Botão para começar aquisição##
start_button = st.empty()
graph = st.empty()
if start_button.button("Start Recording"):
   client = mqtt.Client("Comando_gravar")
   client.connect(MQTT_broker)
   client.publish("daniafurkaaib/start", payload = "start")
   time.sleep(7)
   plotdata()



   
   
   
   
    

