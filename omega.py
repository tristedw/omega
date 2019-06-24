#!/usr/bin/env python3

# made by tristan edwards
import snowboydecoder
import speech_recognition
import configparser
import time
import wolframalpha
import urllib
import re
from commands.tts import text_to_speech
from commands.smart_home import device_control
from commands.smart_home import chromecast
from commands.common import recognize_lists, weather


config = configparser.ConfigParser()
config.read('config.ini')
wra_client = wolframalpha.Client(config.get('api_keys', 'wolframalpha'))


def recognize_callback():
    recognizer = speech_recognition.Recognizer()
    dynamic_energy = config.get('recognizer', 'dynamic_energy')
    dynamic_energy_threshold = config.get('recognizer', 'dynamic_energy_threshold')
    energy_threshold = config.get('recognizer', 'energy_threshold')
    with speech_recognition.Microphone() as mic_source:
        if dynamic_energy == "True":
            print("Dynamic energy == True")
            recognizer.energy_threshold = float(dynamic_energy_threshold)

        elif dynamic_energy == "False":
            recognizer.energy_threshold = float(energy_threshold)

        print("Energy threshold = " + str(recognizer.energy_threshold))
        print("Listening...")
        text_to_speech.mixer.init()
        text_to_speech.mixer.music.load('audio/on.wav')
        text_to_speech.mixer.music.play()
        text_to_speech.speech_control('pause')
        audio = recognizer.listen(mic_source, timeout=6, phrase_time_limit=15.5)
        text_to_speech.mixer.init()
        text_to_speech.mixer.music.load('audio/recog.wav')
        text_to_speech.mixer.music.play()
    try:
        recognizer_result = recognizer.recognize_google(audio).lower()
        print(recognizer_result)
# smart home
        if 'turn off the ' in recognizer_result:
            device_off = str(recognizer_result).replace('turn off the ', '').split()
            if 'on' in recognizer_result:
                for item, elem in enumerate(recognize_lists.bad_device_list):
                    while elem in device_off:
                        device_off.remove(elem)
                        print(device_off)
                if recognizer_result.find('on') < recognizer_result.find(device_off[0]):
                    del device_off[0]
                    print(device_off)
                if recognizer_result.find('on') > recognizer_result.find(device_off[0]):
                    del device_off[1]
                    print(device_off)
                for device in device_off:
                    device_control.toggle(device, 'off')
            else:
                for device in device_off:
                    device_control.toggle(device, 'off')

        if 'turn on the ' in recognizer_result:
            device_on = str(recognizer_result).replace('turn on the ', '').split()
            if 'off' in recognizer_result:
                for item, elem in enumerate(recognize_lists.bad_device_list):
                    while elem in device_on:
                        device_on.remove(elem)
                        print(device_on)
                if recognizer_result.find('off') < recognizer_result.find(device_on[0]):
                    del device_on[0]
                    print(device_on)
                if recognizer_result.find('off') > recognizer_result.find(device_on[0]):
                    del device_on[1]
                    print(device_on)
                for device in device_on:
                    device_control.toggle(device, 'on')
            else:
                for device in device_on:
                    device_control.toggle(device, 'on')

        if 'chromecast stream ' in recognizer_result:
            cut = recognizer_result.replace('chromecast stream ', '')
            if 'movie' in cut:
                movie = cut.replace('movie', '')
                print(movie)
                text_to_speech.tts("Searching and streaming movie " + movie)
                chromecast.chromecast_control('movie', movie)
            if 'youtube' in cut:
                string = cut.replace("youtube ", "")
                query_string = urllib.parse.urlencode({"search_query": string})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                url = "http://www.youtube.com/watch?v=" + search_results[0]
                print(url)
                chromecast.chromecast_control('youtube', url)
                text_to_speech.tts("streaming " + string + " from youtube")

# common
        if any(time_result in recognizer_result for time_result in recognize_lists.time_list):
            text_to_speech.tts(time.strftime("%I:%M %p"))

        if any(date_result in recognizer_result for date_result in recognize_lists.date_list):
            text_to_speech.tts(time.strftime("%a %b %d %Y"))
# weather
        if any(weather_result in recognizer_result for weather_result in recognize_lists.weather_list):
            weather.recieve_weather()

        if "what is" in recognizer_result:
            query = recognizer_result.replace("what is", "")
            res = wra_client.query(query)
            answer = next(res.results, None).text
            text_to_speech.tts(answer)

        if "who is" in recognizer_result:
            query = recognizer_result.replace('who is', '')
            res = wra_client.query(query)
            answer = next(res.results, None).text
            text_to_speech.tts(answer)

        if recognizer_result == 'stop':
            text_to_speech.speech_control('stop')
            pass

    except speech_recognition.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except speech_recognition.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except AttributeError:
        print('ugh oh...')
    except configparser.NoOptionError:
        print('no device...')


model = 'Omega.pmdl'
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Waiting for keyword....')

detector.start(detected_callback=recognize_callback,
               sleep_time=0.03)
detector.terminate()
