from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import os
import pyttsx3


window=Tk()

window.title("Text to Speech Coverter")
window.geometry("900x450+200+200")
window.resizable(False,False)
window.config(bg="#8B0000")

engine=pyttsx3.init()

def speaknow():
    text=text_box.get(1.0,END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender == "Male"):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()



def download():
    text=text_box.get(1.0,END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender == "Male"):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()



#Top Frame
top_frame=Frame(window,bg="#FFEFD5",width=900,height=100)
top_frame.place(x=0,y=0)




main=Label(window,text="TEXT TO SPEECH CONVERTER",font=("Times New Roman",28,"bold"))
main.place(x=100,y=30)
main.config(bg="#FFEFD5",fg="#8B0000")

#text_box
text_box=Text(window,font=("Times New Roman",20, "bold"),relief=GROOVE,wrap=WORD)

text_box.place(x=10,y=150,width=500,height=250)
text_box.config(bg="#FFEFD5",fg="#8B0000")

voice=Label(window,text="VOICE",font=("Times New Roman",15,"bold"),bg="#8B0000",fg="#FFEFD5")
voice.place(x=580,y=160)

speed=Label(window,text="SPEED",font=("Times New Roman",15,"bold"),bg="#8B0000",fg="#FFEFD5")
speed.place(x=760,y=160)


gender_box=Combobox(window,values=['Male','Female'],state='r',font=("Times New Roman",14),width=10)
gender_box.place(x=550,y=200)
gender_box.set("Male")


speed_box=Combobox(window,values=['Fast','Normal','Slow'],state='r',font=("Times New Roman",14),width=10)
speed_box.place(x=730,y=200)
speed_box.set("Normal")


speak=Button(window,text="SPEAK",width=10,font=("Times New Roman",14,"bold"),command=speaknow)
speak.place(x=550,y=280)
speak.config(bg="#FFEFD5",fg="#8B0000")

save=Button(window,text="SAVE",width=10,font=("Times New Roman",14,"bold"),command=download)
save.place(x=730,y=280)
save.config(bg="#FFEFD5",fg="#8B0000")

window.mainloop()

 