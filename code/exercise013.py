#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 22:52:03 2018

@author: MikeNagler
"""

import thinkdsp
from thinkdsp import Wave, Signal, Spectrum 

sin_sig = thinkdsp.SinSignal(freq=600, amp=1.0, offset=0) 
cos_sig = thinkdsp.SinSignal(freq=800, amp=0.5, offset=0) 
mix = sin_sig + cos_sig 
mix_wave = mix.make_wave(duration=1, start=0, framerate=11025) 

mix_wave.write('temp.wav') 
thinkdsp.play_wave(filename='temp.wav', player='afplay') 

spectrum = mix_wave.make_spectrum() 
spectrum.plot(high=1000) 