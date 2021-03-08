import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from quickdraw import QuickDrawData
import SpInput as si
import models as md

qd = QuickDrawData()
r = sr.Recognizer()
myMic = sr.Microphone(device_index=1) 

audio = si.audio
ar=md.ResNet(audio)
qr = r.recognize_google(audio)
words = word_tokenize(qr)
out = nltk.pos_tag(words)
print(out)