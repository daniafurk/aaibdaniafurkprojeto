import paho.mqtt.client as mqtt
import time 
import csv 
import pandas as pd 
import json

MQTT_broker = 'test.mosquitto.org'
now = time.time()


def on_connect(client, userdata, flags,rc):
    print(f"Connected with result code  {str(rc)} to MQTT broker on {MQTT_broker}")

def on_message(client, userdata, msg): 
     #writedata(msg.payload.decode())
     ##Aqui estou a repôr as minhas features em listas, pq antes tinha transformado em str 
     m = msg.payload.decode()
     m_list = json.loads(m)
     print("Recieved Message")
     tofile(m_list)
     
     
     
#Para criar um ficheiro csv e as suas colunas    
def headers():
    try:
        with open('values.csv','r') as csv_file:
            pass
    except:       
         with open('values.csv', mode ='w', newline='') as csv_file:
            fieldnames = ['sample','valor']
            writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
            writer.writeheader()

#Para escrever nesse csv
def writedata(a):
    file = open("values.csv")
    reader = csv.reader(file)
    sample = len(list(reader))
    sample+=1
    with open('values.csv', mode='a', newline='') as csv_file:
        csv_file_writer = csv.writer(csv_file, delimiter= ',')
        csv_file_writer.writerow([sample,a])
        
def tofile(a):
   with open('pmvalues.csv', 'w', newline='') as file_object:
       writer_object = csv.writer(file_object)
       for line in a:
           writer_object.writerow(line)
        
client = mqtt.Client("stream")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_broker)
client.subscribe("daniafurkaaib/audiofeatures")
client.loop_forever()


   



