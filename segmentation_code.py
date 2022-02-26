

#---segmentation code----

#importing of all necessary libraries  
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
  
#loading and converting heart sounds 
  
#finding sounds with the extension 'mp3' in the path mentioned. 
audio_files = librosa.util.find_files('/Users/shreeyarao/Desktop/heart sounds', ext=['mp3']) 
  
#conversion of the sounds into array 
heart_sounds = np.asarray(audio_files) 
  
#segmentation of heart sounds 
  
f = 37  #gives the heart sound number 
audio_data , sr = librosa.load(heart_sounds[f] , sr = 2000) #loading the sound and sampling it  
  
  
n = np.arange(len(audio_data)) #returns an ndarray of evenly spaced numbers in the given interval 
  
envp_sounds = [] #list which will contain the filtered signals 
  
#signal.filtfilt will filter the signal 
envp_sounds = signal.filtfilt(np.ones(100)/100 , [1] , audio_data**2) #using signal.filtfilt 
  
#find_peaks function used to find the peak in the signal 
peaks = signal.find_peaks(envp_sounds , distance = 2000)#finding peaks  
  
peak_pos = peaks[0] #gives peak positions    
  
#plotting of the figure which shows the peaks in the signal 
fig = plt.figure() 
ax = fig.subplots() 
ax.plot(n , audio_data)  #plots the audio data 
ax.plot(n ,envp_sounds)   #plots the filtered audio data 
ax.scatter(n[peak_pos] , envp_sounds[peak_pos] , c = 'k')   #plots the peaks in the audio data 
plt.show() #displays the plots 
  
temp = [] #list which will contain the segmented heart sound 
  
#segmenting the heart sound file using each of its peak.  
for p in peak_pos: 
    temp.append(audio_data[p-1200:p+1200])  
  
#temp file at the end has details of each of the heart cycles in a particular sound file 
plt.figure() 
#saving the segmented heart sound details in a file 
  
#plotting of each of the heart cycles in the heart sound file 
  
k = 0 
for t in temp: 
    plt.plot(t) 
    plt.show()  
    file = open("heart_sound"+str(f) + "_" +str(k) , "w" ) 
    np.savetxt(file , t)   
    k = k + 1 
 
 