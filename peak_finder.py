
#PEAK FINDING CODE

import os
import pywt
from matplotlib import pyplot as plt
import numpy as np
import librosa 
import librosa.display
from scipy import signal
import matplotlib
import scipy
import time


plt.close()
audio_folder_path = ('/Users/shreeyarao/Desktop/heart sounds')
audio_files = librosa.util.find_files('/Users/shreeyarao/Desktop/heart sounds', ext=['mp3']) 

heart_sounds = np.asarray(audio_files)

f = 1

audio_data , sr = librosa.load(heart_sounds[f] , sr = 2000) #loading the sound 

n = np.arange(len(audio_data))
envp_sounds = []
envp_sounds = signal.filtfilt(np.ones(100)/100 , [1] , audio_data**2) #using signal.filtfilt 
peaks = signal.find_peaks(envp_sounds , distance = 1000) #finding peaks 
peak_pos = peaks[0] #gives peak positions   

fig = plt.figure()
ax = fig.subplots()
ax.plot(n , audio_data)
ax.plot(n ,envp_sounds)
ax.scatter(n[peak_pos] , envp_sounds[peak_pos]) 
plt.show()

temp = []
for p in peak_pos:
    temp.append(audio_data[p-375:p+1000])
    
plt.figure()
for t in temp:
    plt.plot(t)
    plt.show()

