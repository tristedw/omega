# omega
python voice assistant with IOT compatability V0.1, just made it

# about
A python voice assistant, which is capable of controlling sonoff devices flashed with the [tasmota](https://github.com/arendst/Sonoff-Tasmota) firmware or even non modified Wemo smart plugs as well as other features and more to come.

# installation
1. install portaudio dependencies 
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
The keyword is "Omega" so once the application states that it is "Listening..." speak "Omega" wait for the ding sound and ask it a command.
# commands
The current commands you can ask it is:
1. Turn on or off a smart device configureable ip in the config.ini file
2. Weather based on geoip and using openweathermap
3. Date and time.
# WIP commands
Soon to be released commands, also I do have this working currently but they are not stable:
1. Chromecast streaming with Youtube, Spotify and Plex
2. SMS recieving and sending...
3. Calculator
4. Timer
5. Playing music
6. IFTTT compatability
If you want another feature feel free to ask.
