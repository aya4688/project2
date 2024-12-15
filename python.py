from tkinter import *
import tkinter as tk
import pyttsx3
def speek():
    te=pyttsx3.init()
    te.say(entry_widget.get())
    te.runAndWait()
def exit_program():
    root.destroy() 
def clear_text():
    entry_widget.delete(0, tk.END)   

root=tk.Tk()       
root.title("text to speech")
root.geometry("350x500")
mylabal=Label(root,text=" Enter your text:")
mylabal.pack(pady=30)
entry_widget=Entry(root,width=30)
entry_widget.pack(pady=20)
mybutton1=Button(root,text="play",command=speek).place(x=95,y=150)

mybutton2=Button(root,text="Exit",bg="red",command=exit_program).place(x=150,y=150)

mybutton3=Button(root,text="set",command=clear_text).place(x=200,y=150)





root.mainloop()


