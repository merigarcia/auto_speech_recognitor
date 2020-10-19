## Introduction for runing speech_recognition script <h2> 
*This script tool has been developed by PhD student in BCBL [Meritxell Garcia](https://www.bcbl.eu/es/conocenos/equipo/meritxell-garcia) for transcripting single/multiple .wav files into txt/excel*


#### Attention: <h3>
```diff
+ Please make sure you have connected internet/wifi
+ This script is written in Python 3
+ Before runing it, make sure to have installed the following packages: *numpy, speech_recognition, scipy, pandas*. 
+ Make sure for both scripts to be saved in the same folder. 
+ The script "speech_recognition_func.py" includes the function of transcription. The script "run_speech_recognition.py" is the one you need to run with your own .wav data
```
 
### To run the script **"run_speech_recognition.py"**, follow the steps:
1. Open **"run_speech_recognition.py"** with any type of editor (spyder, pycharm, notepad++ ...).
2. Edit the three variables:
  - `<filepath>`: add your audio path.
  - `<language>`: put the code of your audios language. By default is  "es"(spanish). Check the following webpage all the available language codes for transcription when meets your need:                  https://cloud.google.com/translate/docs/languages
  - `<outputpath>`: add the path where you want your results to be saved.

*Note*: You can set the format of your output files (xlsx, txt...)

