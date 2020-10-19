#!usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:14:27 2020
Speech recognition script
@author: Meritxell Garcia Perea
"""

####################################################
###           RT_Stroop task            ###
###             Author: Meri Garcia              ###               
####################################################
from __future__ import print_function

import os, glob
import numpy as np
import speech_recognition as sr
import scipy.io.wavfile
import time
import pandas as pd

def interpret_audios(filepath, language, outpath):
    print ("This function needs 3 variables: filepath, language, outpath")   
    filename = []
    num = []
    words = []
    
    # To add your audio path, now it only supports .wav format audios.
    filenames = sorted(glob.glob(filepath)) #Choose the folder of the audio files to process
    t0 = time.time()
    
    print("\n ######################################################################")
    print("\n #######      Start of audio interpretation, good luck!         #######")
    print("\n ######################################################################\n")
    
    print("\nDear,\n")
    print("To use this script, please make sure a good connection of internet/wifi!\n")
    print("Are you ready? The following will be your list of audio content.\n")
    print("It may take some time, be patient & enjoy it!\n")
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    
    print("Current version of Google speech recognition package is:  ", sr.__version__)
    for f in filenames:
        
        recd = 0
        tmp_num=0
        # Firstly, we use Scipy package to get the audio duration time
        (source_rate, source_sig) = scipy.io.wavfile.read(f)
        
        duration_seconds = len(source_sig) / float(source_rate)
        print("\n", os.path.basename(f))
        #print("duration time: ", source_sig.size)    
        
        t = round(duration_seconds, 4)  # Initial parameter of audio duration time (seconds)
        output=open(outpath,'a') #Folder where you want to save the output
        #print("\n", os.path.basename(f), file=output)
        
        print("duration time: ",t) 
        
        c = 0  # to count the iteration times (try times in case of failed)
        while True:
            
            if t>0:
                try:
                    sr.enable_word_time_offsets = True
                    VF = sr.AudioFile(f)
                    r = sr.Recognizer()
                    with VF as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.record(source, duration=t) #, timeout=None)#duration=t)
       
                    recd = r.recognize_google(audio, language = language)
                    tmp_num = len(recd.split(" "))
                    
                    print("count of words:{},   duration time {} seconds".format(tmp_num, t))
                    print(recd)
                    
                    print("count of words:{},   duration time {} seconds".format(tmp_num, t), file=output)
                    print(recd, file=output)
                    
                    break
                except:
                    c+=1
                    print("The {} time try, but failed again".format(int(c)))
                    t-=0.1  # once the interpretor stops working, we try to optimize the duration times                     
            else:
                tmp_num = 0
                recd = 0
                print("\n T_T Bad luck! This audio is not understood, although we tried our best.")            
                break
            break
        output.close()
        base = os.path.basename(f)
        filename.append(os.path.splitext(base)[0])
        num.append(int(tmp_num))
        words.append(recd)
        
    print("\n Summary of Results \n")
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    
    print(filename)
    print(num)
    print(words)
    t1 = time.time()
    cput = round((t1- t0)/60,2)
    
    words = np.array(words)
    database = np.matrix([filename, num, words]).transpose() #Output composed by audio name, number of total words, words transcription
    data = pd.DataFrame(database)
    data
    
    writer = pd.ExcelWriter(outpath, engine="xlsxwriter") #Folder for saving the output
    data.to_excel(writer, index=False)
    writer.save()
    
    print("\n ###################################################################### \n")
    print("       Bravo! We finished interpretation of {} audios in {} min".format(len(num), cput))
    print("            Buy a cup of capuccino for our developer! ")
    print("\n ###################################################################### \n")
    

    return 0
#EOF
