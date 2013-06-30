---
layout: post
title: Tipping Bucket Rain Gauge - Part 1
tags:
  - tipping bucket
  - rain gauge
  - DIY
  - hacks
  - 3D printer
---

I currently have a Raspberry Pi set up to drive my lawn sprinklers using [an OpenSprinkler Pi](http://rayshobby.net/mediawiki/index.php?title=OpenSprinkler_Pi) system.
I wrote some basic scripts to check the weather and decide whether or not it would be a good idea to water the lawn that day.  However, the weather reported does not always match what is experienced for the whole city so I decided to set up my own rain gauge.

### Parts list
1. [Tipping bucket](http://www.thingiverse.com/thing:85045)
2. Rod threaded on one end (something like this [aileron control rod](http://www.hobbyking.com/hobbyking/store/__34929__super_scout_w_camera_1400mm_replacement_aileron_control_rod_set.html))
3. Nuts to fit rod
4. Teflon washers to space things out
5. Rare earth magnet
6. Reed switch
7. Some sort of electronics setup, like and arduino that can compute your rainfall
8. CD spindle (50+ cd count) to house things and keep them dry
9. A funnel

I got items 2, 3, and 4 at hobbyworld in Saskatoon.  5, 6, and 9 were donated by srw7, a friend from the local hackerspace.  I had an arduino around for 7.  And I found a funnel in the kitchen that hasn't been missed... yet.

### Step 1 - Print the part
Get out your 3D printer and let loose some plastic.  The part is [here](http://www.thingiverse.com/thing:85045).

Here is what it looks like printed.

<a href="http://www.flickr.com/photos/59175237@N00/9177600248/" title="Untitled by _apollo_, on Flickr"><img src="http://farm4.staticflickr.com/3807/9177600248_04414d385d.jpg" width="500" height="375" alt="Untitled"></a>

### Step 2 - Epoxy the magnet to the bucket
The location depends on where you will get the best read.  You can put it at the top and have it count every tip back and forth.  Or put it at one end and have a back and forth tip count as 1 in your math.


### Step 3 - Find and modify a container
I ended up using an empty 50-CD spindle.  The black spindle itself was drilled and used to mount the bucket and reed switch.  The lid was used for weather proofing with a hole drilled in to mount the funnel through.

Pic of drilled spindle.

Pic of drilled lid.

### Step 4 - Contruct the mechanical parts
Bend and cut rod to fit bucket, use teflon washers to space things appropriately.  Use the nuts to fix the rod to the spindle.  Epoxy the funnel in place.

Pics of above.

Test with water!

Video of test.

### Step 5 - Connect electronics

This is a work in progress, currently have an arduino connect to count tips and calculate rainfall.

The formula used is

    rainfall = number_of_tips * volume_per_tip / collecting_area_of_funnel


