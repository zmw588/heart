# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:15:47 2021

@author: 417-02
"""
'''
import pickle

with open('usr_info.pickle', 'rb') as usr_file:
    exist_usr_info = pickle.load(usr_file)
print(exist_usr_info)
'''
'''
import turtle
import tkinter as tkinter

root = tkinter.Tk()
root.geometry('500x500-5+40') #added by me
cv = turtle.ScrolledCanvas(root, width=900, height=900)
cv.pack()

screen = turtle.TurtleScreen(cv)
screen.screensize(2000,1500) #added by me
t = turtle.RawTurtle(screen)
t.hideturtle()
t.circle(100)

root.mainloop()
'''
import tkinter as tk


def onResize(event):
    """Prints the scrollbar's position on window resize."""
    print(str(myScrollbar.get()))


root = tk.Tk()
myFrame = tk.Frame(root)
mySecondaryFrame = tk.Frame(root)
myCanvas = tk.Canvas(myFrame)
myScrollbar = tk.Scrollbar(myFrame, orient='vertical', command=myCanvas.yview)

myCanvas.config(yscrollcommand=myScrollbar.set)

for i in range(0,100):
    print(i)
    button = tk.Button(mySecondaryFrame, text=i)
    button.pack(fill='y',expand=True)
    myCanvas.configure(scrollregion=(0, 0, 0, 3000))

myFrame.pack(fill='both',expand=True)
myScrollbar.pack(side="right",fill='y')
myCanvas.pack(side='right', fill='both', expand=True)

button_window = myCanvas.create_window(0, 0, anchor='nw', window=mySecondaryFrame)

myCanvas.bind('<Configure>', onResize)

tk.mainloop()