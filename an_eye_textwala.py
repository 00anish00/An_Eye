# achiving wd files
import sys
sys.path.append("wd")

# speaker
import voiceoutput as vc
def speak(aud):
    vc.spk(aud)

# task runner 
import task as tk


# write and speak at a time
import speakandwrite as sw
def dic(text):
    sw.dictate(text)


if __name__ =='__main__':
    print('YOU ARE USING AN_EYE A POTENTIAL PERSONAL ASSISTANT BROWSING SYSTEM FOR YOUR PERSONAL COMPUTER')
    print("_A___R__")
    speak('             YOU ARE USING N EYE A POTENTIAL PERSONAL ASSISTANT BROWSING SYSTEM FOR YOUR PERSONAL COMPUTER')
    
    while True:    
        tk.run()
        break
