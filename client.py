import pyttsx3
import requests
import customtkinter
from customtkinter import CTk

def changeWord():
    print()

def commit():
    print()

def readWord():
    print()







#GUI -------------------------------------------------------------------------------------------------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

APP = customtkinter.CTk()

APP.title("LOC")
APP.geometry("800x750")

button1 = customtkinter.CTkButton(master=APP, text="Commit",
                                     width=100, height=100, font=("", 30),command=changeWord)
button1.place(relx=0.25, rely=0.8, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(master=APP, text="Change",
                                    width=100, height=100, font=("", 30),command=commit)
button2.place(relx=0.75, rely=0.8, anchor=customtkinter.CENTER)

button3 = customtkinter.CTkButton(master=APP,text="READ AGAIN"
                                    ,width=50,height=50,font=("",15),command=readWord)
button3.place(relx=0.15,rely=0.1, anchor=customtkinter.CENTER)

box= customtkinter.CTkEntry(master=APP,width=170,height=50,placeholder_text="Type Here")
box.place(relx=0.5,rely=0.5, anchor=customtkinter.CENTER)

APP.mainloop()