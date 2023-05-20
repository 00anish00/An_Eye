import voiceoutput as vc
def speak(aud):
    vc.spk(aud)

def dictate(text):
    print(text)
    speak(text)
    # for text in range(text):
    #     speak(text)
    #     for text in range(text):
    #         print(text)
# dictate(" naish kharpadu")