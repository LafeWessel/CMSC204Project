# -*- coding: utf-8 -*-
"""
Spyder Editor

This file contains the code for the Tic Tac Toe UI and how it interacts with the server
"""

#Imports and initialization of tkinter object
from tkinter import *

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.initWindow()
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
#        self.pack(fill=BOTH,expand =1)
        self.pack()
        
        button1 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button1))
        button2 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button2))
        button3 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button3))
        button4 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button4))
        button5 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button5))        
        button6 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button6))
        button7 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button7))
        button8 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button8))
        button9 = Button(self, text=" ", height=4, width=8, command=lambda: btnClick(button9))
        buttonQuit = Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = Button(self, text = "restart",command=lambda: restart())
        
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
        buttonRestart.grid(row=0, column=2)
    
    
    def restart():
        print("restart clicked")
    
    def btnClick(Button):
        print("button has been clicked")
        
    #Sends choice back to server
    def submitChoice(choiceLocation):
        print("Choice Submitted")
    
    #Disables buttons, for at end of match
    def disableButtons():
        print("Buttons disabled")
        
    #Enables buttons, for at start of match
    def enableButtons():
        print("Buttons enabled")
    
root = Tk()
root.geometry("500x500")
app = Window(root)
app.mainloop()