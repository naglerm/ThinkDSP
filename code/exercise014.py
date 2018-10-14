import thinkdsp 
from thinkdsp import Wave, Spectrum, Signal 

def stretch(wave, factor):
    wave.ts *= factor  
    wave.framerate /= factor 

"""test the function""" 

wave = thinkdsp.read_wave(filename='guitar_sound.wav') 
thinkdsp.play_wave(filename='guitar_sound.wav', player='afplay') 
stretch(wave, 2) 
wave.write(filename='temp.wav') 
thinkdsp.play_wave(filename='temp.wav', player='afplay') 