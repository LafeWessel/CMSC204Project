# -*- coding: utf-8 -*-
"""
Spyder Editor

This file contains the code for the Tic Tac Toe UI and how it interacts with the server
"""

#Imports and initialization of tkinter object
from tkinter import *
from functools import partial



class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.buttonValues = [" "," "," "," "," "," "," "," "," "]
        self.arrayOfButtons = []
        self.initWindow()
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
        self.pack()
        button0 = Button(self, text=self.buttonValues[0], height=6, width=12, command=lambda: btnClicked(0))
        button1 = Button(self, text=self.buttonValues[1], height=6, width=12, command=lambda: btnClicked(1))
        button2 = Button(self, text=self.buttonValues[2], height=6, width=12, command=lambda: btnClicked(2))
        button3 = Button(self, text=self.buttonValues[3], height=6, width=12, command=lambda: btnClicked(3))
        button4 = Button(self, text=self.buttonValues[4], height=6, width=12, command=lambda: btnClicked(4))        
        button5 = Button(self, text=self.buttonValues[5], height=6, width=12, command=lambda: btnClicked(5))
        button6 = Button(self, text=self.buttonValues[6], height=6, width=12, command=lambda: btnClicked(6))
        button7 = Button(self, text=self.buttonValues[7], height=6, width=12, command=lambda: btnClicked(7))
        button8 = Button(self, text=self.buttonValues[8], height=6, width=12, command=lambda: btnClicked(8))
        
        self.arrayOfButtons.append(button0)
        self.arrayOfButtons.append(button1)
        self.arrayOfButtons.append(button2)
        self.arrayOfButtons.append(button3)
        self.arrayOfButtons.append(button4)
        self.arrayOfButtons.append(button5)
        self.arrayOfButtons.append(button6)
        self.arrayOfButtons.append(button7)
        self.arrayOfButtons.append(button8)

        buttonQuit = Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = Button(self, text = "Restart",command=lambda: self.restart())
        
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
        
        #This keeps the user from inputting any data until the server gives it permission to
        self.disableButtons()
        
    #should change the value of the empty button to be the player's and then tell the server what changed
    def btnClicked(buttonClicked):
        print("button has been clicked")
        #If the spot is not take, it will assign the new value and update the board, otherwise nothing happens
        
            
    #Erases local board and tells server to delete memory and begin a new instance of the game
    def restart(button):
        print("restart clicked")
        eraseBoard()        
        
    #Sets the boards values to whatever is in the buttonValues list
    def updateBoard():
        print("Board Updating")  
        
    #Should set all board values back to " "     
    def eraseBoard():
        print("Erasing board")
        self.buttonValues = [" "," "," "," "," "," "," "," "," "]
        updateBoard()
        
    #Sends choice back to server
    def submitChoice(choiceLocation):
        print("Choice Submitted")
    
    
    #Disables buttons, for at end of match
    def disableButtons(self):
        print("Buttons disabled")
        for button in self.arrayOfButtons:
            button.config(state=DISABLED)
            print("%s was disabled",button)
        
    #Enables buttons, for at start of match
    def enableButtons():
        print("Buttons enabled")
        for button in self.arrayOfButtons:
            button.config(state="normal")


        

        
#global buttonValues = [" "," "," "," "," "," "," "," "," "]

root = Tk()
root.geometry("400x350")
app = Window(root)
app.mainloop()