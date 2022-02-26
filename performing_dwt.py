import os 
import pywt 
from matplotlib import pyplot as plt 
import numpy as np 
import librosa  
import librosa.display 
from scipy import signal 


audio_data = ('/Users/shreeyarao/Desktop/s.mp3')
audio_data , sr = librosa.load(audio_data, sr = 2000 ) 
audio_data = audio_data[0:10000] 
audio_data_array = np.array(audio_data) 
cA,cD = pywt.dwt(audio_data,'coif5', mode='symmetric', axis = -1) 

plt.figure(figsize = (11,11)) 
plt.subplot(10,1,1) 
librosa.display.waveplot(cA, sr) 
 
 