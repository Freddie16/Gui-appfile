
import tkinter as tk
from tkinter import filedialog,Text, mainloop
import os

root = tk.Tk()
apps =[]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

        
    filename = filedialog.askopenfilename(initialdir="/",title="Select file",
    filetypes=(("executables","*.exe"),("all files","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()


canvas = tk.Canvas(root,height=500,width=400,bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root,text="Open file",padx=10,pady=5,fg="white",bg="#263D42")
openFile.pack()

runApps = tk.Button(root,text="Run Apps",padx=10,pady=5,fg="white",bg="#263D42")
runApps.pack()

root =mainloop()