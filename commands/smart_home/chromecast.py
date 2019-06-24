#!/usr/bin/env python3
import pychromecast
import configparser
import requests
import os.path
from pychromecast.controllers.youtube import YouTubeController

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../../config.ini')
cast_name = config.get('smart_home', 'chromecast_name')
flextv_server_ip = config.get('smart_home', 'flextv_server_ip')
flextv_api_token = config.get('api_keys', 'flextv_api')


def chromecast_control(command, info):
    if command == "movie":
        requests.post("http://" + flextv_server_ip + "/FlexTV/api.php?say&web=true&command=play+" + 
                      command + "&apiToken=" + flextv_api_token)
    if command == "youtube":
        video_id = info
        chromecasts = pychromecast.get_chromecasts()
        cast = next(cc for cc in chromecasts if cc.device.friendly_name == cast_name)
        cast.wait()
        yt = YouTubeController()
        cast.register_handler(yt)
        yt.play_video(video_id)

    if command == "command":
        chromecasts = pychromecast.get_chromecasts()
        cast = next(cc for cc in chromecasts if cc.device.friendly_name == cast_name)
        cast.wait()
        print('Connected to ' + cast_name)
        mc = cast.media_controller
        if info == 'pause':
            print("pausing")
            mc.block_until_active()
            mc.pause()
        if info == 'play':
            print("playing")
            mc.block_until_active()
            mc.play()
        if info == 'stop':
            print("stopping")
            mc.block_until_active()
            mc.stop()
        if info == 'skip':
            print("skipping")
            mc.block_until_active()
            mc.skip()
        if info == 'rewind':
            print("rewinding")
            mc.block_until_active()
            mc.rewind()
