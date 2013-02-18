#!/bin/env python
import os
import time


connected =False
counter = 0
os.system("amixer cset numid=3 1")
os.system("amixer set Master 100%")
os.system("pacmd set-sink-volume 0 65537")

# while (connected =FALSE)

#edit wait time, to search for devices 1 unit = 2 sec , 3 would give six seconds
WAIT=4

while(counter<=WAIT):
	response=os.popen('pactl list sources short')
	text=response.read()
	if(text.find("bluez")<0):
		print("i am sleeping")
		time.sleep(2);
	else:
# edit this line to add your phone's bluetooth MAC		
		os.system("pactl load-module module-loopback source=bluez_source.50_EA_D6_DE_D9_39 sink=alsa_output.platform-bcm2835_AUD0.0.analog-stereo")
	        counter=3
	counter+=1
	
response.close();
