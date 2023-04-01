import datetime as dt
import requests

#BASE="http://api.openweathermap.org/data/2.5/weather?appid=afd745ddab811f2eff33ed9716831752&q=colombo"
Base="http://api.openweathermap.org/data/2.5/weather?appid="
#url = BASE

print("Please read the Instruction to get an API \n")
api=input ("Enter API:")
city=input ("Enter City:")

url="http://api.openweathermap.org/data/2.5/weather?appid="+api+"&q="+city

response = requests.get(url).json()

print(response)
