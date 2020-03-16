#Text to speach assistant
import pyttsx3

class Calvin:
    en_zira_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.en_zira_id)
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 1.0)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()



# 
# from gtts import gTTS
# import os
# tts = gTTS(text='Algo', lang='es')
# tts.save("good.mp3")
# os.system("good.mp3")
