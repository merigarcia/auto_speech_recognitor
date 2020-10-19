#!/usr/bin/env python
# coding: utf-8

import os, glob
import numpy as np
import speech_recognition as sr
import scipy.io.wavfile
import time
import pandas as pd
from speech_recognition_func import interpret_audios


# You have to call three functions: 
# -filepath
# -language
# -outpath


filepath = 'G:\\Path_name\\Folder_name\\*.wav'
language = 'es'  # https://cloud.google.com/translate/docs/languages
outpath =  'F:\\Path_name\\Folder_name\\results.xlsx'


interpret_audios(filepath, language, outpath)






