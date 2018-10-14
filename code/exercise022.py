import thinkdsp 
import math 
from thinkdsp import Sinusoid 
import numpy as np

class SawToothSignal(Sinusoid):
    """class definition for sawtooth signal"""
    def evaluate(self, ts):
        # frac is an array that answers the question, at each index,
        # what FRACTION of the current cycle am I on? basically just 
        # moves from 0..1 a bunch at a linear rate
        # cycles goes from 0..X a bunch, frac just takes the fraction part
        cycles = self.freq * ts + self.offset / (2 * math.pi) 
        frac, _ = np.modf(cycles)
        # now we pretty much have what we want, except we need to bias it 
        # so it is centered at 0 and then scale it up to the amplitude we need 
        ys = thinkdsp.unbias(frac) 
        ys = thinkdsp.normalize(ys, self.amp)  
        return ys

signal1 = SawToothSignal(freq=440, amp=1, offset=0) 
wave = signal1.make_wave(duration=1, start=0, framerate=11025) 
signal1.plot()
spec = wave.make_spectrum() 
spec.plot(high=3000) 


