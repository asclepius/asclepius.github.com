---
layout: post
title: Raspberry Pi Install Details
categories:
  - raspberrypi
---
This is a post detailing how we installed the Raspberry Pi software using Mac OS X Mountain Lion.
The raspberry pi site has an excellent quick-start guide [http://www.raspberrypi.org/quick-start-guide].

## Equipment Used ##

* Raspberry Pi Model B
* 8 GB class 10 microSD card with standard SD adapter
* USB-based microSD card reader to write the image to
* USB keyboard and mouse
* HDMI cable
* MicroUSB cable and wall power source 


## Installation ##

1. Download an install image, we used Raspbian "wheezy" from [here](http://www.raspberrypi.org/downloads)
2. Various options for loading the SD card are given [here](http://elinux.org/RPi_Easy_SD_Card_Setup).  We unzipped the imaged and used dd to install it as they describe for Mac OS X.
3. Put the card into the Pi
4. Connect HDMI, power, ethernet, keyboard, and mouse
5. Plug it in, HDMI did not work initially.  
6. SSH into the box with username: pi, password: raspberry (for raspbian wheezy)
7. Run the following command:
  sudo raspi-config
8. In raspi-config you can set up all the options as you like.  Change to a US keyboard layout for US/Canada. (I select generic 105, then "Other" then "English (US)".  If you have a big SD card make sure you expand the file system to utilize this.
9. After the ssh setup the HDMI worked fine.  Not sure why it did not work initially.
    

