# omega
python voice assistant with IOT and Chromecast compatability V0.2

# about
A python voice assistant, which is capable of controlling sonoff devices flashed with the [tasmota](https://github.com/arendst/Sonoff-Tasmota) firmware or even non modified Wemo smart plugs. You can also cast to a chromecast with ethier setting up and using [FlexTV](https://github.com/d8ahazard/FlexTV) to cast to Plex, or you can cast directly from YouTube. Aswell as many other features.

# installation
  1. install PyAudio and dependencies 
```
sudo apt-get install libasound-dev
```
  2. download portaudio from [here](http://portaudio.com/download.html)
  3. unzip the archive
```
tar -zxvf [portaudio.tgz](will not be called this)
```
  4. enter the directory
  5. configure and make
```
./configure && make
```
  6. install
```
sudo make install
```
  7. install again
```
sudo pip install pyaudio
```
  8. git clone this repository
```
git clone https://github.com/kanrinsha/omega.git && cd omega
```
  9. install dependencies
```
pip install -r requirements.txt
```
  10. open config.ini and enter api keys for provided services
  11. run omega.py
```
python omega.py
```
# usage
The keyword is "Omega" so once the application states that it is "Listening..." speak "Omega" wait for the ding sound and ask it a command. You may need to setup snowboy and add the files from the installation into the omega directory, if so watch [this](https://www.youtube.com/watch?v=mUEm05ZAhhI) video. If you want to cast to Plex you will need to install both the Chromecast plugin for Plex and also setup FlexTV, which can be done [here](https://github.com/d8ahazard/FlexTV). Omega also does not record conversations outside of you saying the keyword, as it is using [snowboy](https://snowboy.kitt.ai/).
# commands
The current commands you can ask it is: (You have to say the hotword and hear the 'ding' before asking)

  1. Turn on or off a smart device configureable ip in the config.ini file
  
    Say 'Turn off [device]' to turn a configured device off
    Say 'Turn on' [device]' to turn a configured device on
    
  2. Cast to a chromecast with Plex, or YouTube.
  
    Say 'chromecast stream youtube [youtube video name or channel name]'(will get the latest video if you say channel)
    Say 'chromecast stream movie [movie name]'
    
  3. Weather based on geoip and using openweathermap
  
    Say anything close to what's the weather (multiple keywords for less remembering)
    
  4. Wolframalpha
    
    Say 'what is [thing]'
    Say 'who is [thing]'
    
  5. Date and time.
  
    Say anything close to what's the time
    
# WIP commands
Soon to be released commands, also I do have this working currently but they are not stable:

  ~~1. Chromecast streaming with Youtube, Spotify and Plex~~ V0.2
  
  2. SMS recieving and sending...
  
  3. Calculator
  
  4. Timer
  
  5. Playing music
  
  6. IFTTT compatability
  
