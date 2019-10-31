# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Imports and initialization of tkinter object
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

class Application(tk.frame):
    
    button1,button2,button3,button4,button5,button6,button7,button8,button9
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createButtons()
    
    #creates and lays out buttons
    def createButtons(self):
        button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
        button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
        button3 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
        button4 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
        button5 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
        button6 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
        button7 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
        button8 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
        button9 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
 #       buttonQuit = Button(tk, text="Quit", font='Times 10 bold', bg='gray', fg='white', height=0, width=4, command=self.master.destroy))
        
        button1.grid(row=3,column=0)
        button2.grid(row=3,column=1)
        button3.grid(row=3,column=2)
        button4.grid(row=4,column=0)
        button5.grid(row=4,column=1)
        button6.grid(row=4,column=2)
        button7.grid(row=5,column=0)
        button8.grid(row=5,column=1)
        button9.grid(row=5,column=2)
        buttonQuit.grid(row=0,column=0)
    
        
    #Sends choice back to server
    def submitChoice(choiceLocation):
        print("Choice Submitted")
    
    #Disables buttons, for at end of match
    def disableButtons():
        print("Buttons disabled")
        
        
    
        
    #Enables buttons, for at start of match
    def enableButtons():
        print("Buttons enabled")
    

tk.mainloop()