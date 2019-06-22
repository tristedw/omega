#!/usr/bin/env python3
import subprocess
import pyowm
import configparser
import os.path
import requests
import json
from commands.tts import text_to_speech

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../../config.ini')
owm = pyowm.OWM(config.get('api_keys', 'openweathermap'))
ipstack_key = config.get('api_keys', 'ipstack')
GET_IP_CMD = "hostname -I"


def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def recieve_weather():
    ip = str(run_cmd(GET_IP_CMD)).split(' ')[1]
    print(ip)
    response = requests.get('http://api.ipstack.com/' + ip + '?access_key=' + ipstack_key)
    dump = json.loads(response.text)
    city = str(dump["city"])
    country = str(dump["country_code"])
    city_and_country = city + ', ' + country
    print(city_and_country)

    open_weather_map = owm.weather_at_place(city_and_country)
    get_weather = open_weather_map.get_weather()
    get_weather_details = get_weather.get_detailed_status()
    print(get_weather_details)
    get_temperature = get_weather.get_temperature(unit='celsius')
    print(get_temperature['temp'])
    text_to_speech.tts("The weather for " + city + " is " + str(get_weather_details) + " with a temperature of " + str(
        get_temperature['temp']) + " degrees celsius")
