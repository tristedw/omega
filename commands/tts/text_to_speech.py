#!/usr/bin/env python3
from gtts import gTTS
from pygame import mixer
import alsaaudio
import os.path
# for raspberry pi
am = alsaaudio.Mixer()
voice_path = os.path.dirname(__file__) + '/../../audio/'


def tts(speech):
    text_to_speak = gTTS(text=speech, lang='en-us')
    text_to_speak.save(voice_path + 'voice.mp3')
    mixer.init()
    mixer.music.load(voice_path + 'voice.mp3')
    mixer.music.play()
    print(speech)


def speech_control(command):
    if command == 'pause':
        mixer.pause()
    if command == 'stop':
        mixer.stop()
