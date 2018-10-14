#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:38:29 2018

@author: MikeNagler
"""
import thinkdsp 
from thinkdsp import Signal, Wave, Spectrum 

tri_sig = thinkdsp.TriangleSignal(freq=440)
tri_wave = tri_sig.make_wave(duration=0.01, start=1, framerate=11025) 
tri_wave.plot()

tri_spec = tri_wave.make_spectrum() 
tri_spec.plot()
print(tri_spec.hs[0])

tri_wave.write('temp.wav') 
thinkdsp.play_wave('temp.wav', 'afplay') 

tri_spec.hs[0] = 100 
tri_spec.plot()
tri_wave2 = tri_spec.make_wave() 
tri_wave2.plot()

tri_wave2.write(filename='temp2.wav') 
thinkdsp.play_wave('temp2.wav', 'afplay') 

