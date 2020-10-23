from gtts import gTTS
from playsound import playsound
mytext = ["earliest","institution","similar","generous"]
language ='en'
for i in mytext:
    tts = gTTS(i, lang='en')
    hlo = i+".mp3"
    tts.save(hlo)

