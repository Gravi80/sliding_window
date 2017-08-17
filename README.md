### Status
[![Build Status](https://travis-ci.org/ravi2020/sliding_window.svg?branch=master)](https://travis-ci.org/ravi2020/sliding_window)

**Usage**
=========
    $ pip install window-slider
    
$ python

       >>> from window_slider import Window
       >>> list = [0, 1, 2, 3, 4, 5, 6, 7]
       >>> bucket_size = 3
       >>> overlap_count = 1
       >>> window = Window(list,bucket_size,overlap_count)       
       >>> while True:
       >>>     window_matrix = window.slide()
               # do your stuff
       >>>     if window.reached_end_of_list(): break