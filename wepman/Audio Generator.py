from gtts import gTTS
from playsound import playsound
mytext = ["rub","rug","mat","map","back","back","done","bun","web","wed","with","with","beg","bed","come","comb","park","park","other","over","gun","done","mine","nine","boat","goat","shave","save","seat","feet","deaf","death","van","than","wing","wing","cheek","cheap","bridge","bridge","prize","prize","pick","kick","reach","reach","free","three","thread","shred","foal","fall","went","went","call","call","pass","path","tar","tar","ten","pen","pat","pet","sat","sack","buff","bus","din","din","rose","rose","thank","sank","mars","marsh","coast","toast","ten","tin"]
language ='en'
for i in mytext:
    tts = gTTS(i, lang='en')
    hlo = i+".mp3"
    tts.save(hlo)

