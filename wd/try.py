# import pyaudio
# pyaudio.get_portaudio_version()
# pa = pyaudio.PyAudio()
# pa.get_default_host_api_info()

# for id in range(pa.get_host_api_count()):
#     print(pa.get_host_api_info_by_index(id))

# pa.get_default_output_device_info()  

# for id in range(pa.get_device_count()):
#   dev_dict = pa.get_device_info_by_index(id)
#   for key, value in dev_dict.items():
#       print(key, value)

# import wave
# wav_file = wave.open('wd\Jai Shree Ram - Notification.wav')
# stream_out = pa.open(
#     rate=wav_file.getframerate(),     # sampling rate
#     channels=wav_file.getnchannels(), # number of output channels
#     format=pa.get_format_from_width(wav_file.getsampwidth()),  # sample format and length
#     output=True,             # output stream flag
#     output_device_index=4,   # output device index
#     frames_per_buffer=1024,  # buffer length
# )
# output_audio = wav_file.readframes(5 * wav_file.getframerate())
# stream_out.write(output_audio)




# stream_in = pa.open(
#     rate=48000,
#     channels=2,
#     format=pyaudio.paInt16,
#     input=True,                   # input stream flag
#     input_device_index=1,         # input device index
#     frames_per_buffer=1024
# )

# # read 5 seconds of the input stream
# input_audio = stream_in.read(5 * 48000)



# output_filename = 'audio-recording.wav'
# wav_file = wave.open(output_filename, 'wb')

# # define audio stream properties
# wav_file.setnchannels(2)        # number of channels
# wav_file.setsampwidth(2)        # sample width in bytes
# wav_file.setframerate(48000)    # sampling rate in Hz

# # write samples to the file
# wav_file.writeframes(input_audio)

# import pyttsx3

# def speak_hindi(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Adjust the speech rate (optional)
#     engine.setProperty('volume', 1.0)  # Adjust the volume (optional)
#     engine.setProperty('voice', 'hi')  # Set the voice to Hindi (hi)
#     engine.say(text)
#     engine.runAndWait()

# # Example usage
# text = "नमस्ते! कैसे हो?"
# speak_hindi(text)
# import pyaudio
# import speech_recognition as sr

# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1  # Adjust the pause threshold if needed
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en')  # Adjust language if needed
#         print(f"User said: {query}")
#         return query.lower()
#     except sr.UnknownValueError:
#         print("Sorry, I didn't catch that. Please try again.")
#         return ""
#     except sr.RequestError as e:
#         print("Sorry, my speech service is currently unavailable. Please try again later.")
#         return ""

# # Example usage
# command = take_command()
# print(command)


# import voiceoutput as vc
# def speak(aud):
#     vc.spk(aud)
# speak('Type the message querry or problem to pruh·seed further')

# import turtle

# # Set up the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("")  # Set the background color

# # Create a turtle object
# dot = turtle.Turtle()
# dot.shape("circle")  # Set the shape of the turtle to a circle
# dot.color("purple")  # Set the color of the dots

# # Move the turtle and draw dots
# dot.penup()  # Lift the pen
# dot.goto(-200, 0)  # Move the turtle to the starting position

# # Draw 100 dots
# for _ in range(100):
#     dot.pendown()  # Put the pen down
#     dot.dot(10)  # Draw a dot
#     dot.penup()  # Lift the pen
#     dot.forward(20)  # Move the turtle forward

# # Close the turtle graphics window
# turtle.done()

# Define the width and height of the visual representation


# import time
# column = 100
# row = 1

# # Create the visual representation
# for row in range(row):
#     for col in range(column):
#         time.sleep(0.001)
#         print(".", end="")
    # print()  # Move to the next line


# # Define the number of dots to display
# num_dots = 100

# # Create the visual representation
# for i in range(num_dots):
#     print(".", end="")
#     time.sleep(0.5)  # Delay for half a second between each dot

# print()  # Move to the next line after all dots are displayed


# import task as tk
# # qry=tk.qery()
# # print(qry)
# tk.run() 

# import keyboard

# def on_key(event):
#     if event.name == 'esc':
#         print("Escape key pressed. Exiting...")
#         # Add your code to handle the Esc key press event
#         keyboard.unhook_all()  # Stop listening for key events
#         exit()
# keyboard.on_press()
# keyboard.wait()  # Wait for any key press
# a=keyboard.get_hotkey_name()
# if  a =='esc':
#     exit()

# import keyboard

# def press(key):
#     if key.name == 'esc':
#         print("esc key pressed.")
#         return 'esc'
        
# keyboard.on_press(press)
# keyboard.wait()











# Processing dots *
# import process_dots as pd
# def dots():
#     pd.dots()

# # Output audio *
# import voiceoutput as vc
# def speak(text):
#     vc.spk(text)

# # text insert taker *
# def qery():
#     a=str(input("enter.....:"))
#     return a

# # write and speak at a time
# import speakandwrite as sw
# def dic(text):
#     sw.dictate(text)

# # ---------------modules_imported_and_created---------------------------------------------------------------------------------------
# # ------------------------------------task-modules-------------------------------------------------------------

# # tk1
# import wikipedia
# # tk2
# import webbrowser
# # tk exit
# import keyboard
# import sys
# import time




# def run():
    
#     # qryf = filtered query
#     # iv=qery()
    
#     # speak('Type the message querry or problem to pruh·seed further')
    
#     while True:
        
#         print("Type the message querry or problem to procced further  || To Close Press 'ESC' key")
#         # keyboard.wait(3)
#         if keyboard.is_pressed('q'):
#             print('Have a good time')
#             time.sleep(2)
#             sys.exit()
#         else:
#             qry=qery()

#             if 'wikipedia' in qry  or 'Wikipedia' in qry or 'WIKIPEDIA' in qry :
#                 # tk1
#                 qryf=qry
#                 try:
#                     results = wikipedia.summary(qryf,sentences=4)
#                     dic("As per the wikipedia",)
#                     dic(results)

#                 except wikipedia.exceptions.WikipediaException as e:
#                     print(e)
#                     dic('Wikipedia can not find it or server connection error ')


#             if 'youtube' in qry: 
#                 # tk2   
#                 dic("opening   youtube")
#                 qryf=qry.replace('youtube','')
#                 webbrowser.open(url=f"https://www.youtube.com/results?search_query={qryf}")





#             else:
#                 try:
#                     qryf=qry
#                     webbrowser.open_new(url=f'https://www.google.com/search?q={qryf}')
#                 except:
#                     print('Sorry for the inconvenience || by-ghatiya developer ')







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
    # while True:
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
        if 'exit' in userinput or 'Exit' in userinput or 'EXIT'in userinput:
            dic("\nByee")
            dots()
            sys.exit()

            # else:
            #     dic("Please Try Again\n")
            #     dots()