import voiceoutput as vc
def speak(aud):
    vc.spk(aud)

# task runner 
import task as tk

# dots
import process_dots as pd
def dots():
    pd.dots()


# write and speak at a time
import speakandwrite as sw
def dic(text):
    sw.dictate(text)

import time


import datetime
# WISH MODULE
def w_time():
    hour = int(datetime.datetime.now().hour)
    wish=""
    if hour == 6 and hour<12:
        wish=("GOOD MORNING ")
    elif hour == 0 and hour <6:
        wish=("GOOD NIGHT")
    elif hour==12 and hour<18:
        wish=("GOOD AFTERNOON")
    else :
        wish=("GOOD EVENING")
    dic(wish)

def date():
    date=datetime.datetime.now().date()
    dic(date)
    

def time():
    time=(datetime.datetime.now().hour)
    dic(f"{time} -O' Clock")
    
# def wish():
#     w_time()
#     t=time().time
#     dic(f"The Time is{t} 'O clock")
def m_wish():
    date(),time(),w_time()
