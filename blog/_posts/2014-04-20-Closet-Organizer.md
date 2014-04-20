---
layout: post
title: Closet Organizer - Bill of Materials Using [OpenSCAD](http://www.openscad.org)
tags:
  - OpenSCAD
  - Carpentry
  - DIY
  - Closet organizer
  - Bash Hacks
---

We are in the process of some renovations and our closets were looking pretty shabby.
I designed a new closet organizer that should allow us to get a little more out of the space we have.

## Bill of Material in [OpenSCAD](http://www.openscad.org)

The [OpenSCAD](http://www.openscad.org) portion of thigns was pretty straightforward.  I added a little functionality by including a bill of material utility. 

Used a modular design so that each shelf was instatiated by itself.  I then added an echo statement to the shelf module to make it spit out its dimensions:

    module top_shelf()
    {
      translate([0,0,sh_tot_height]) cube([sh_depth, cl_rct_ln, sh_width]);
      echo(str("Top shelf: ",sh_depth,units,"x ",cl_rct_ln,units,"x ", sh_width, units));
    };

I then wrote a [script](https://github.com/asclepius/closet_organizer/blob/master/bom.sh) to parse the echo'd text and tally things up with uniq.

The end results for the BOM is:

    ./bom.sh 
       8 Rod bracket: 12 inches x 4 inches x 0.625 inches 
       4 Rod: 1 inches x 30.875 inches 
      10 Shelf bracket: 12 inches x 2 inches x 0.625 inches 
       2 Shelf upright: 12 inches x 80 inches x 0.625 inches 
       5 Shelf: 12 inches x 24 inches x 0.625 inches 
       1 Top shelf: 12 inches x 87 inches x 0.625 inches 
    Total length of 16 inch wood
    387
    Total length of rod
    155.500