---
layout: post
title: Raspbmc Install Notes
categories:
  - raspberrypi
  - raspbmc
---
This is a post detailing the raspbmc installation and a few tweaks so that my lovely wife can set up a few more at her school.

## Equipment Used ##

* Raspberry Pi Model B
* 8 GB class 10 microSD card with standard SD adapter
* USB-based microSD card reader to write the image to
* USB keyboard and mouse
* HDMI cable
* MicroUSB cable and wall power source 


## Installation ##

1. Go [here](http://www.raspbmc.com/wiki/user/os-x-linux-installation/) and do what it says!
* Essentially the important part is the following (**BE SURE OF THE DISK YOU SELECT, OR FACE THE CONSEQUENCES OF DESTROYING YOUR HARDDRIVE**): 

        curl -O http://svn.stmlabs.com/svn/raspbmc/testing/installers/python/install.py
        chmod +x install.py
        sudo python install.py

2. I have a collection of MPEG-2 files so I purchased the additional license as detailed on the [raspberry pi site](http://www.raspberrypi.com/mpeg-2-license-key/).  Edit /boot/config and add your mpeg key there.

3. I could not get any deinterlacing to work on the pi so I decided to set the output resolution to 1080i.  For some reason Raspbmc would not let me do this, to solve it I edited the config.txt file to manually set the resolution.  Details on this file can be found [here](http://elinux.org/RPi_config.txt).

## Hardware setup ##

I have a TV with a USB port for playing files from a disk.  Conveniently, this port supplies enough power to run the Pi!  So no power source is needed just a micro USB cable.

Additionally I have samba storage on the network and use this.
