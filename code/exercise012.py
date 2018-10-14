import thinkdsp 
from thinkdsp import Wave, Signal, Spectrum 

# load sound
guitar_wave = thinkdsp.read_wave('guitar_sound.wav') 

# create a short segment of the sound with constant pitch
short_sound = guitar_wave.segment(5.0, 0.5) # (start, duration) 

# testing
# short_sound.write('temp.wav') 
# thinkdsp.play_wave(filename='temp.wav', player='afplay') ### note that the player is afplay, not aplay as specified in the book 

spectrum = short_sound.make_spectrum() 
spectrum.plot(high=2000)  

"""
Next comes meessing with some filters
"""
spectrum.low_pass(500, 0.1) 
spectrum.plot(high=2000) 

spectrum = short_sound.make_spectrum() 
spectrum.high_pass(250, 0.5) 
spectrum.plot(high=2000) 

spectrum = short_sound.make_spectrum() 
spectrum.band_stop(250, 500, 0.2) 
spectrum.plot(high=2000) 