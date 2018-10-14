#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:59:32 2018

@author: MikeNagler
"""

import thinkdsp 
from thinkdsp import Signal, Wave, Spectrum 

signal1 = thinkdsp.SquareSignal(freq=1100, amp=1.0, offset=0) 
wave1 = signal1.make_wave(duration=1, start=0, framerate=10000) 
spectrum1 = wave1.make_spectrum() 
spectrum1.plot() 

wave1.write(filename='temp.wav') 
thinkdsp.play_wave(filename='temp.wav', player='afplay') 