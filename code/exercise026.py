#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:37:36 2018

@author: MikeNagler
"""

import thinkdsp 
import numpy as np 

fundamental = 110
freqs = np.arange(110, 1100, 110) 
amps = 1/freqs**2

mix = sum(thinkdsp.SinSignal(freq=f, amp=a) for f, a in zip(freqs, amps)) 

wave = mix.make_wave()
segment = wave.segment(duration=0.01)

spectrum = wave.make_spectrum() 
spectrum.plot()

wave.write(filename='temp.wav') 
thinkdsp.play_wave(filename='temp.wav', player='afplay')
    
    

