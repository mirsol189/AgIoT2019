# import modules
import numpy as np
import os
from parse import *
import json
import requests

#weatherAPI
url = 'http://api.openweathermap.org/data/2.5/forecast?zip=47907,us&APPID=65b145c4c3e9787a31a313f5d742e482'
res = requests.get(url)

data=res.json()
date=data['list'][0]['dt_txt']
weather=data['list'][0]['weather'][0]['main']

# set directory
file_name = 'log.txt'

file_opened = open(file_name)
line=file_opened.readline()
line = json.loads(line[line.find('{'):])
#print(line)

temp=line['payload_fields']['temperature_1']
soil=line['payload_fields']['luminosity_3']
hum=line['payload_fields']['relative_humidity_2']
time=line['metadata']['time']

with open("parselog.txt","w") as text_file:
    text_file.write('time:{},'.format(time))
    text_file.write('luminosity_3:{},'.format(soil))
    text_file.write('relative_humidity:{},'.format(hum))
    text_file.write('temperature:{},'.format(temp))
    text_file.write('forecast_date:{},'.format(date))
    text_file.write('forecast_weather:{}'.format(weather))

