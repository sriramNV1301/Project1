import speech_recognition as sr
import quickdraw
from quickdraw import QuickDrawData, QuickDrawDataGroup
import nltk
from nltk.tokenize import word_tokenize

r = sr.Recognizer()
nouns = []
verbs = []
skybox = []
terrain = []
objects = []

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

def skyBox(tags):
    for i in tags:
        if i[0] == 'night' or i[0] == 'day' or i[0] == 'evening' or i[0] == 'morning' or i[0] == 'afternoon':
            skybox.append(i[0])

def terra(tags):
    for i in tags:
        if i[0] == "road" or i[0] == "field" or i[0] == "beach" or i[0] == "monuntain" or i[0] == "sea":
            terrain.append(i[0])

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

print("Skybox: ")
for i in skybox:
    print(i+" ")
print("terrain: ")
for i in terrain:
    print(i+" ")
    
    

