#####Publicação dos dados pelo PC######
import paho.mqtt.client as mqtt
import librosa
import numpy as np
import sounddevice 
from scipy.io.wavfile import write
import json

##DEFINIR AS VARIÁVEIS DE AQUISIÇÃO DE SOM 
fs = 44100 # number of samples recorded in a second 
second = 5 #tempo de gravação
FRAME_SIZE = 512
HOP_SIZE = 128

##Broker
MQTT_broker = 'mqtt.eclipseprojects.io'

##DEFINIR FUNÇÕES MQTT##
def on_connect(client, userdata, flags,rc):
    print(f"Connected with result code  {str(rc)} to MQTT broker on {MQTT_broker}")

def on_message(client, userdata, msg):
    print(msg.topic+" "+ str(msg.payload.decode()))
    #####Gravar áudio#########
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2) 
    sounddevice.wait()
    write("myrec.wav",fs,record_voice)
    print("audio was recorded")
    ##Extrair as features do áudio##
    audio_arr , sr = librosa.load("myrec.wav")
    data = json.dumps(audio_arr.tolist())
    ##Publicar essas features##
    client.publish("daniafurkaaib/audiofeatures", data )
    

client = mqtt.Client("Spectdata")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_broker)
client.subscribe("daniafurkaaib/start")
client.loop_forever()
