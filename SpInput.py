import speech_recognition as sr
r = sr.Recognizer()
myMic = sr.Microphone(device_index=1) 

with myMic as source:
    print("Say Now") 
    audio = r.listen(source)


