# -*- coding: utf-8 -*-
"""
Spyder Editor

This file contains the code for the Tic Tac Toe UI and how it interacts with the server
"""

#Imports and initialization of tkinter object
#from tkinter import *
import tkinter as tk



class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.buttonValues = [" "," "," "," "," "," "," "," "," "]
        self.arrayOfButtons = []
        self.initWindow()
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
        self.pack()
        button0 = tk.Button(self, text=self.buttonValues[0], height=6, width=12, command=lambda: self.btnClicked(0))
        button1 = tk.Button(self, text=self.buttonValues[1], height=6, width=12, command=lambda: self.btnClicked(1))
        button2 = tk.Button(self, text=self.buttonValues[2], height=6, width=12, command=lambda: self.btnClicked(2))
        button3 = tk.Button(self, text=self.buttonValues[3], height=6, width=12, command=lambda: self.btnClicked(3))
        button4 = tk.Button(self, text=self.buttonValues[4], height=6, width=12, command=lambda: self.btnClicked(4))        
        button5 = tk.Button(self, text=self.buttonValues[5], height=6, width=12, command=lambda: self.btnClicked(5))
        button6 = tk.Button(self, text=self.buttonValues[6], height=6, width=12, command=lambda: self.btnClicked(6))
        button7 = tk.Button(self, text=self.buttonValues[7], height=6, width=12, command=lambda: self.btnClicked(7))
        button8 = tk.Button(self, text=self.buttonValues[8], height=6, width=12, command=lambda: self.btnClicked(8))
        
        self.arrayOfButtons.append(button0)
        self.arrayOfButtons.append(button1)
        self.arrayOfButtons.append(button2)
        self.arrayOfButtons.append(button3)
        self.arrayOfButtons.append(button4)
        self.arrayOfButtons.append(button5)
        self.arrayOfButtons.append(button6)
        self.arrayOfButtons.append(button7)
        self.arrayOfButtons.append(button8)

        buttonQuit = tk.Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = tk.Button(self, text = "Restart",command=lambda: self.restart())
        
        button0.grid(row=3,column=0)
        button1.grid(row=3,column=1)
        button2.grid(row=3,column=2)
        button3.grid(row=4,column=0)
        button4.grid(row=4,column=1)
        button5.grid(row=4,column=2)
        button6.grid(row=5,column=0)
        button7.grid(row=5,column=1)
        button8.grid(row=5,column=2)
        buttonQuit.grid(row=0,column=0)
        buttonRestart.grid(row=0, column=2)
        
        
    #should change the value of the empty button to be the player's and then tell the server what changed
    def btnClicked(self, i ):
        print("button has been clicked")
        print(self)
        print(i)
        self.buttonValues[i] = "x"
        
        self.updateBoard()
        self.submitChoice()
        
            
    #Erases local board and tells server to delete memory and begin a new instance of the game
    def restart(self):
        print("restart clicked")
        print(self)
        self.eraseBoard()        
        
    #Sets the boards values to whatever is in the buttonValues list
    def updateBoard(self):
        print("Board Updating")
        print(self)
        index = 0
        for i in self.buttonValues:
            self.arrayOfButtons[index]['text'] = i
            print(self.arrayOfButtons[index])
            print(index)
            index += 1
        
    #Should set all board values back to " "     
    def eraseBoard(self):
        print("Erasing board")
        print(self)
        self.buttonValues = [" "," "," "," "," "," "," "," "," "]
        self.updateBoard()
        
    #Sends choice back to server
    def submitChoice(choiceLocation):
        print("Choice Submitted")
    
    
    #Disables buttons, for at end of match
    def disableButtons(self):
        print("Buttons disabled")
        for button in self.arrayOfButtons:
            button.config(state=tk.DISABLED)
            print("was disabled",button)
        
    #Enables buttons, for at start of match
    def enableButtons(self):
        print("Buttons enabled")
        for button in self.arrayOfButtons:
            button.config(state=tk.NORMAL)

root = tk.Tk()
root.geometry("400x350")
app = Window(root)
app.mainloop()