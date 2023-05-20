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


import task as tk
# qry=tk.qery()
# print(qry)
tk.run() 