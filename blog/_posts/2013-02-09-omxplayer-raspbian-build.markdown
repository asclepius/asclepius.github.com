---
layout: post
title: omxplayer + raspbian build
tags:
  - RPi
  - raspberrypi
  - omxplayer
  - tips
---

I was very impressed by the prompt response I got form the omxplayer team when asking about a windowed output feature.  Then I started trying to build from source and was having a harder time.  The Makefiles are not set up for a standard Raspbian distro.

Found [this](https://github.com/huceke/omxplayer/issues/73#issuecomment-12645858), ffmpeg has built, now some bugs are popping up in the omxplayer source.  
