import pyttsx3
# module for text to speech converter

engine = pyttsx3.init('sapi5')
# Initialize the text-to-speech engine

# voice properties
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Set a slower speech rate
engine.setProperty('rate', 146)
  # Decrease the rate to 100

# print(f"Selected Assistant Voice {voices[1].id}")

# speech out module
def spk(aud):
    engine.say(aud)
    engine.runAndWait()
































