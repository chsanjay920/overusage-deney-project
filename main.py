from face_recognition import *
import time
import cv2
from tkinter import *
from datetime import datetime
from cap import *


c = cap()
def start():
    c.GetUserImage()
    # win.after(10000,start)

win = Tk()
win.title("monitoring..")
win.geometry("400x200")
win.resizable(False,False)
button = Button(win,text="start",width=10,command=start)
button.place(x=25,y=50)
win.mainloop()

