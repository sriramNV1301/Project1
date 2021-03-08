import speech_recognition as sr
from tkinter import *
#import frame2 
import nltk
import os
from quickdraw import QuickDrawData
#######################
from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import quickdraw

qd = QuickDrawData()

window=Tk()
window.title('Main Fram')
window.geometry("750x600")
window.resizable(width = True, height = True)
#############@ menu @ ###############

menubar = Menu(window)  
menubar.add_command(label="About")  
menubar.add_command(label="Quit ( X )", command=window.quit)  
window.config(menu=menubar)  
#mystring = StringVar()

#######################################

name=StringVar()
tag=StringVar()
tokens=StringVar()
acs=StringVar()
def say():
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
        try:
           
            print("Text: "+r.recognize_google(audio_text)) 
            acs=r.recognize_google(audio_text)
            lbl=Label(window, text= "Text_:_"+r.recognize_google(audio_text) +"_;", fg='GREEN', font=("Helvetica", 11))
            lbl.place(x=80, y=10)
            tokens = nltk.word_tokenize(acs)
            tag=nltk.pos_tag(tokens)
            print(tokens)
            print(tag)
            lb1=Label(window, text= "tokens_:_"+str(tokens)+" ;", fg='GREEN', font=("Helvetica", 11))
            lb1.place(x=10, y=130)
            lb1=Label(window, text= "tags_:_"+str(tag)+" ;", fg='GREEN', font=("Helvetica", 11))
            lb1.place(x=10, y=160)
            
            
        except:
            print("Sorry, I did not get that")
            lbl=Label(window, text= "Sorry, I did not get that", fg='GREEN', font=("Helvetica", 11))
            lbl.place(x=80, y=10)

############################
ext = ".jpg"
def text_say():
    
    text = name.get()
    tokens = nltk.word_tokenize(text)
    print(tokens)
    print(name.get())
    tag=nltk.pos_tag(tokens)
    print(tag)
    for i in tag:
        if i[1] == 'NN' or i[1] == 'NNP':
            obj= qd.get_drawing(i[0])
            obj.image.save(i[0]+ext)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp  =nltk.RegexpParser(grammar)
    result = cp.parse(tag)
    print(result)
    #result.draw()
    
    #cp =nltk.RegexpParser(tokens)
    #result = cp.parse(tag)
    #print(result)
    lb1=Label(window, text= "Text:_"+str(text)+" ;", fg='GREEN', font=("Helvetica", 11))
    lb1.place(x=80, y=10)
    lbl2=Label(window, text="tokenize:_"+str(tag)+";", fg='GREEN', font=("Helvetica", 11))
    lbl2.place(x=10, y=130)
    #lbl=Label(window, text="gramer"+*tag+, fg='GREEN', font=("Helvetica", 11))
    #lbl.place(x=10, y=160)
#################################################################################
def canv():
    os.system('py frame3.py')        

########################@ Button @##################################
#txtfld=Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=80, y=150)
#btn=Button(window, text="This is Button widget", fg='blue')
#btn.place(x=80, y=100)


bt1=Button(window, text="Speak", fg='blue',command=say)
bt1.place(x=10, y=10)

bt2=Button(window, text="ENTER", fg='blue',command=text_say)
bt2.place(x=10, y=50)

bt3=Button(window, text="test the image", fg='blue',command=canv)
bt3.place(x=50, y=90)

#bt4=Button(window, text="<< PROVES", fg='blue')
#bt4.place(x=510, y=530)

#bt5=Button(window, text="NEXT >>", fg='blue')
#bt5.place(x=610, y=530)
################################ai
def simp_ai():
    os.system('py frame2.py')
#C:/Users/saisunil/Desktop/final cut/frame2.py
   
    
bt6=Button(window, text="SIMPLE A_I", fg='blue',command=simp_ai)
bt6.place(x=510, y=530)

############################################################



########################@ input @##################################

txt1=Entry(window , textvariable=name)
txt1.place(x=80, y=50)

############ @ lable @ ######################

lbl=Label(window, text="© All right having app was developed by CHARAN M , SRIRAM N V ,SAISUNIL S ", fg='GREEN', font=("Helvetica", 11))
lbl.place(x=175, y=580)


#############################################




window.mainloop()