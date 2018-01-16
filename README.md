### Status
[![Build Status](https://travis-ci.org/codewithravi/sliding_window.svg?branch=master)](https://travis-ci.org/codewithravi/sliding_window)
[![PyPI](https://img.shields.io/pypi/v/window-slider.svg)](https://pypi.python.org/pypi/window-slider)
[![last commit](https://img.shields.io/github/last-commit/codewithravi/sliding_window.svg?label=last%20commit)](https://github.com/codewithravi/sliding_window/commits/master)
[![License](https://img.shields.io/hexpm/l/plug.svg)](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0))

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
