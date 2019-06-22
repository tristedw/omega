# omega
python voice assistant with IOT compatability

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
10. run omega.py
```
python omega.py
```
