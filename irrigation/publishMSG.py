import paho.mqtt.client as paho
import json

file_name = 'parselog.txt'

file_opened = open(file_name)
line=file_opened.readline()

print(line)
broker="192.168.2.62"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("Contorl1")                         #create client object
client1.username_pw_set("agiot","2019")
client1.on_publish = on_publish               #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("dev/test",payload=line, qos=0, retain=False)                #publish
