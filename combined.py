import speech_recognition as sr
import quickdraw
from quickdraw import QuickDrawData, QuickDrawDataGroup
import nltk
from nltk.tokenize import word_tokenize

r = sr.Recognizer()
nouns = []
verbs = []

def speechInput():
    myMic = sr.Microphone(device_index=1) 

    with myMic as source:
        print("Say Now") 
        audio = r.listen(source)
    return audio

def speechToText(audio):
    text = r.recognize_google(audio)
    words = word_tokenize(text)
    POStags = nltk.pos_tag(words)
    return POStags

def textNouns(POStags):
    for i in POStags:
        if i[1] == 'NN' or i[1] == 'NNP':
            nouns.append(i[0])

def textVerbs(POStags):
    for i in POStags:
        if i[1] == 'VBG':
            verbs.append(i[0])

audio = speechInput()
tags = speechToText(audio)
textNouns(tags)
textVerbs(tags)

print(tags)

print("nouns: ")
for i in nouns:
    print(i+" ")

print("Verbs: ")
for i in verbs:
    print(i+" ")

