import paho.mqtt.client as mqtt
import csv 
import json
import numpy as np

MQTT_broker = 'mqtt.eclipseprojects.io'

def on_connect(client, userdata, flags,rc):
    print(f"Connected with result code  {str(rc)} to MQTT broker on {MQTT_broker}")

def on_message(client, userdata, msg): 
     ##Aqui estou a repôr as minhas features em listas, pq antes tinha transformado em str 
     m_list =json.loads(msg.payload.decode())
     print("Recieved Message")
     print(np.shape(np.array(m_list)))
     soundtofile(m_list)
     #tofile(m_list)
           
def soundtofile(a):
    np.savetxt("test.csv",a, delimiter = ',')
        
        
client = mqtt.Client("stream")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_broker)
client.subscribe("daniafurkaaib/audiofeatures")
client.loop_forever()


   



