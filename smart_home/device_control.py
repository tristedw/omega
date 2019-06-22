#!/usr/bin/env python3
import requests
import subprocess
import configparser
import os.path

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../../config.ini')


def toggle(device, command):

    device_ip = config.get('smart_home', device)
    try:
        # sonoff with tasmota
        if command == 'off':
            requests.post('http://' + device_ip + '/cm?cmnd=Power%20Off')
        if command == 'on':
            requests.post('http://' + device_ip + '/cm?cmnd=Power%20On')
    except configparser.NoOptionError:
        pass
        print('no device...')
    except requests.ConnectionError:
        # wemo smart plug
        if command == 'off':
            subprocess.call(["bash", "wemo.sh", device_ip, "OFF"], cwd=os.path.dirname(__file__))
        if command == 'on':
            subprocess.call(["bash", "wemo.sh", device_ip, "ON"], cwd=os.path.dirname(__file__))
