---
layout: post
title: Raspberry Pi Traffic Lights
categories:
  - raspberrypi
  - raspbmc
  - wiring
  - blinkenlights
---
This is a short tutorial on how to set up the Raspberry Pi to make some lights blink using the GPIO

## Materials ##
* Configured RPi 
* Breadboard
* 3 LEDs (red, yellow, green)
* Three 68 Ohm resistors
* Jumper wires

## Steps ##

1. Wire the circuit so that the three LEDs are connect on the positive side to 3.3 V then through the negative side they connect to one of the resistors, and from here to the Wiring pins 0, 1, and 2.  The pinout is detailed [here](https://projects.drogon.net/raspberry-pi/wiringpi/pins/) the 5V pin is the one in the corner of the header nearest the corner of the board.
James explains his circuit in [this YouTube video](http://www.youtube.com/watch?v=xcSML0CZ1L0&feature=share&list=UUFg-ZpDBtVhNa_DZg3_ElIg).

2. Open a terminal (if you need help, GOOGLE!)

3. We used WiringPi and WiringPi-Python for this.  They are installed on the Pi's at Greystone Heights alrady.  Google them to install on your own system!  You may need the python-dev package as well.

3. Mrs. Kulyk's Makerspace Pi's should have the code installed, but it is [here]({{ site.baseurl }}/files/traffic.py) as well if needed.  Change to the directory where the file hangs out:
        
        cd ~/src/traffic

4. Run the code as root.  It needs to be root because the GPIO is access via /dev/mem, a special file that has access to all the lowlevel bits and bytes, giving everyone access would be dangerous.  The "sudo" bit means run it as root (or super user).

        sudo python traffic.py

5.  See if you can figure out how to make the lights blink at different speeds.  Can you turn multiple lights on at a time?  Can you turn them into christmas lights instead of traffic lights?



## Tips ##

* Ctrl-C will stop the program.
* Make sure you shutdown the pi properly or you could fry the sd card. (Or corrupt the filesystem).
* A USB key (you will need a USB hub so you can use keyboard mouse and usb stick at the same time) will allow you to take your code home!


