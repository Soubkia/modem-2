#chip-test.py
import numpy as np
import math
from scipy.signal import chirp, sweep_poly
import matplotlib.pyplot as plt

t = np.linspace(
		0, 		# Start
		2*np.pi, 	# End
		5001 	# Resolution, number of samples generated
	)

w = chirp(
		t, 					# Times to evaluate waveform
		f0=1, 				# Frequency (Hz) at t=0
		t1=1, 				# Time at which f1 is specified
		f1=1, 				# Frequency (Hz) at time t1
		method='linear',	# {linear, quadratic, logarithmic, hyperbolic}, optional
		phi=(np.pi/2)			# Phase offset
	)

s0 = np.sin(t)
s1 = np.sin(2*t)

s_ = (s0 + s1)/2

plt.plot(t,s_)
plt.show()
