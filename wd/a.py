# achiving wd files
import sys
sys.path.append("wd")

# speaker
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


if __name__ =='__main__':
    print('YOU ARE USING AN_EYE A POTENTIAL PERSONAL ASSISTANT BROWSING SYSTEM FOR YOUR PERSONAL COMPUTER')
    print("_A___R__")
    speak('             YOU ARE USING N EYE A POTENTIAL PERSONAL ASSISTANT BROWSING SYSTEM FOR YOUR PERSONAL COMPUTER')
    dots()
    while True:    
        speak('Type "Start" To Continue or "exit" To Quit')
        userinput=input("\nType 'Start' To Continue  || 'exit' To Quit\nType here:.....")
        if 'start' in userinput or 'Start' in userinput or 'START' in userinput:
            dots()
            tk.run()
            break
        elif 'exit' in userinput or 'Exit' in userinput or 'EXIT'in userinput:
            dic("\nByee")
            dots()
            sys.exit()
        else:
            dic("Please Try Again\n")
            dots()