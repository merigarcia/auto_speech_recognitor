#!usr/bin/python

####################################################
###           Auto Speech Recognition            ###
###             Author: Meri Garcia              ###               
####################################################


import os, glob
import numpy as np
import speech_recognition as sr
import scipy.io.wavfile
import time


# To use this script, you'll have to make sure of the connection of internet/wifi

filename = []
num = []

# To add your audio path, now it only supports .wav format audios.
filenames = sorted(glob.glob('Your audio PATH/*.wav'))
t0 = time.time()

print("\n ######################################################################")
print("\n #######      Start of audio interpretation, good luck!         #######")
print("\n ######################################################################\n")

print("\nDear my friend,\n")
print("To use this script, please make sure a good connection of internet/wifi!\n")
print("Are you ready? The following will be your list of audio content.\n")
print("It may take some time, be patient & enjoy it!\n")
print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

for f in filenames:
    
    # Firstly, we use Scipy package to get the audio duration time
    (source_rate, source_sig) = scipy.io.wavfile.read(f)
    duration_seconds = len(source_sig) / float(source_rate)
    
    t = round(duration_seconds, 2)  # Initial parameter of audio duration time (seconds)
    print("\n", os.path.basename(f))
    
    c = 0  # to count the iteration times (try times in case of failed)
    while True:
        
        if t>0:
            try:
                VF = sr.AudioFile(f)
                r = sr.Recognizer()
                with VF as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.record(source, duration=t)
                    
                # Here you will need to change the language you need to translate, by default is English (En)
                recd = r.recognize_google(audio, language = "en")
                tmp_num = len(recd.split(" "))
                print("count of words:{},   duration time {} seconds".format(tmp_num, t))
                print("\n", recd)
                break
            except:
                c+=1
                print("The {} time try, but failed again".format(int(c)))
                t-=1  # once the interpretor stops working, we try to optimize the duration time
                      # at least, maybe we can get some words anyway, despite of incompleteness.
                continue            
        else:
            tmp_num = 0
            print("\n T_T Bad luck, my friend! This audio is not understood, although we tried our best.")            
            break
        break
            
    base = os.path.basename(f)
    filename.append(os.path.splitext(base)[0])
    num.append(int(tmp_num))

print("\n Summary of Results \n")
print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

print(filename)
print(num)
t1 = time.time()
cput = round((t1- t0)/60,2)

print("\n ###################################################################### \n")
print("       Bravo! We finished interpretation of {} audios in {} min".format(len(num), cput))
print("            Buy a cup of capuccino for our developer! ")
print("\n ###################################################################### \n")



#EOF
