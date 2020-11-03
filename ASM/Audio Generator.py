from gtts import gTTS
from playsound import playsound
mytext = ['2,6,5']
language ='en'
for i in mytext:
    tts = gTTS(i, lang='en')
    hlo = i+".mp3"
    tts.save(hlo)

