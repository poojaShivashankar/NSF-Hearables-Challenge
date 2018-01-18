# import wave # not required as scipy is called later
import numpy
import scipy.io.wavfile as siw # have to import every specific package separately
import matplotlib.pyplot as plt

Fs,y = siw.read('HC_samp_modded.wav')
plt.plot(y[:50000])
plt.show()
