import pyaudio
import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjust the pause threshold if needed
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')  # Adjust language if needed
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError as e:
        print("Sorry, my speech service is currently unavailable. Please try again later.")
        return ""

# Example usage
command = take_command()
print(command)
