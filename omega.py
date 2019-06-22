#!/usr/bin/env python3

# made by tristan edwards
import snowboydecoder
import speech_recognition
import configparser
import time
import wolframalpha
from commands.tts import text_to_speech
from commands.smart_home import device_control
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
        audio = recognizer.listen(mic_source, timeout=7.5, phrase_time_limit=15.5)
    try:
        recognizer_result = recognizer.recognize_google(audio).lower()
        print(recognizer_result)
# smart home
        if 'turn off the ' in recognizer_result:
            device_off = recognizer_result.replace('turn off the ', '').replace(' ', '_')
            device_control.toggle(device_off, 'off')
        if 'turn on the ' in recognizer_result:
            device_on = recognizer_result.replace('turn on the ', '').replace(' ', '_')
            device_control.toggle(device_on, 'on')
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


model = 'Omega.pmdl'
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Waiting for keyword....')

detector.start(detected_callback=recognize_callback,
               sleep_time=0.03)

detector.terminate()
