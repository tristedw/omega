#!/usr/bin/env python3
import speech_recognition
import configparser
import os.path

config_path = os.path.dirname(__file__) + '/../config.ini'
config = configparser.ConfigParser()
config.read(config_path)

recognizer = speech_recognition.Recognizer()


def set_energy():
    with speech_recognition.Microphone() as mic_source:
        recognizer.adjust_for_ambient_noise(mic_source)
        config.set('recognizer', 'dynamic_energy_threshold', str(recognizer.energy_threshold))
        with open(config_path, 'w') as configfile:
            config.write(configfile)
        print(recognizer.energy_threshold)


set_energy()
