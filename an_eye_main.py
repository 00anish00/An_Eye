import sys
sys.path.append("wd")


import voiceoutput as vc
def speak(aud):
    vc.spk(aud)

import voiceinput as tc
def tci():
    tc.takecommand()
import task as tk
def run():
    tk.run()
    
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")


# test
# speak('ansjnf')

if __name__=='__main__':
    while True:
        
        tci()
        if (tci() == "exit" or "exit" or "quit" or "leave" ):
            exit()
        elif (tci()=="ani" or "aneye" or "anye" or "anai"):
            run()
        else :
            speak("abtak ghatiya stage me hi he")   
            break




