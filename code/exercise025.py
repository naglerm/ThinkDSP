#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:06:16 2018

@author: MikeNagler
"""

import thinkdsp
from thinkdsp import Signal, Wave, Spectrum

def modify_spectrum(spectrum):
    spectrum.hs[0] = 0
    for i in range(1, len(spectrum.fs)):
        spectrum.hs[i] = spectrum.hs[i] / spectrum.fs[i] 

signal = thinkdsp.SquareSignal() 
signal.plot() 

wave = signal.make_wave(duration=1) 
wave.plot() 

wave.write(filename='temp.wav')

spectrum = wave.make_spectrum() 
print(spectrum.hs[1000]) 
spectrum.plot()

# print(spectrum.fs[10] == 10) ### ok, so fs is just an array of all the frequencies

modify_spectrum(spectrum)
print(spectrum.hs[1000])
spectrum.plot(color='red')
wave2 = spectrum.make_wave() 
wave2.plot()

wave2.write(filename='temp2.wav') 

thinkdsp.play_wave(filename='temp.wav', player='afplay') 
thinkdsp.play_wave(filename='temp2.wav', player='afplay') 
