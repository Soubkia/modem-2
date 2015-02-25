#chip-test.py
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.fftpack import fft, rfft, ifft, irfft

t = np.linspace(
		0, 					# Start
		2*np.pi, 			# End
		500  				# Resolution, number of samples generated
	)

s0 = np.cos(t)
s1 = np.cos(2*t)

s_ = (s0 + s1)/2

#print rfft(s_)

#plt.plot(t,rfft(s_))
#plt.show()

y = s_
period = 2*np.pi

def cn(n):
   c = y*np.exp(-1j*2*n*np.pi*time/period)
   return c.sum()/c.size

def f(x, Nh):
   f = np.array([2*cn(i)*np.exp(1j*2*i*np.pi*x/period) for i in range(1,Nh+1)])
   return f.sum()

y2 = np.array([f(time,50).real for time in t])

plt.plot(t, y)
plt.plot(t, y2)
plt.show()