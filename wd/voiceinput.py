# import voiceoutput as vc
# def speak(aud):
#     vc.spk(aud)
# def engine():
#     vc.engine()


import speech_recognition as sr

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(src)        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in' or 'hn-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        
        return "None" #None string will be returned
    return query

a=takecommand()
print(a)