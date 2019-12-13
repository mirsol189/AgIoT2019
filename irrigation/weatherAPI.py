import requests

url = 'http://api.openweathermap.org/data/2.5/forecast?zip=47907,us&APPID=65b145c4c3e9787a31a313f5d742e482'
res = requests.get(url)

data=res.json()
date=data['list'][1]['dt_txt']
weather=data['list'][0]['weather'][0]['main']

with open("weather.txt","a") as text_file:
    text_file.write('{}\n'.format(date))
    text_file.write('{}\n'.format(weather))


#print("Date: {}\n".format(data))
print('Data : {}'.format(date))
print('Weather : {}'.format(weather))