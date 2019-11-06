"""
import socket
host = '127.0.0.1'
port = 12345
mySocket = socket.socket()
mySocket.connect((host.port))
message = input(" ? ")
while message != 'q':
	mySocket.send (message.encode())
	data = mySocket.recv(1024).decode()
	print('Received from server: ' + data)
	message = input(" ? ")
mySocket.close

import pickle
y = []
data = pickle.dumps(y)
s.send(data)
"""

"""
Spyder Editor

This file contains the code for the Tic Tac Toe UI and how it interacts with the server
"""

"""TODO section

    Write server-client data transaction code
    
"""

#Imports and initialization of tkinter object
import tkinter as tk
from tkinter import ttk
import pickle
import socket


buttonList = []

class Window(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.originalList = ["","","","","","","","",""]
        self.characterList = self.originalList
        self.font = "helvetica 40 bold"
        self.master = master
        self.numberOfGames = 5
        self.playerWins = 0
        self.serverWins = 0
        self.WLText = "W:"+str(self.playerWins)+" L:"+str(self.serverWins)
        self.initWindow()
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
        self.pack()
        hght = 1
        wdth = 3
        
        buttonList.append(tk.Button(self, text=self.characterList[0],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[0])))
        buttonList.append(tk.Button(self, text=self.characterList[1],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[1])))
        buttonList.append(tk.Button(self, text=self.characterList[2],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[2])))
        buttonList.append(tk.Button(self, text=self.characterList[3],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[3])))
        buttonList.append(tk.Button(self, text=self.characterList[4],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[4])))
        buttonList.append(tk.Button(self, text=self.characterList[5],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[5])))
        buttonList.append(tk.Button(self, text=self.characterList[6],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[6])))
        buttonList.append(tk.Button(self, text=self.characterList[7],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[7])))
        buttonList.append(tk.Button(self, text=self.characterList[8],font = self.font, height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[8])))

        print(buttonList)
        buttonQuit = tk.Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = tk.Button(self, text = "Restart",command=lambda: self.restart())
        winsLossesText =tk.Text(self, height = 5, width = 10)
        winsLossesText.insert(tk.END,self.WLText)
        winsLossesText.config(state=tk.DISABLED)
        
        buttonList[0].grid(row=3,column=0)
        buttonList[1].grid(row=3,column=1)
        buttonList[2].grid(row=3,column=2)
        buttonList[3].grid(row=4,column=0)
        buttonList[4].grid(row=4,column=1)
        buttonList[5].grid(row=4,column=2)
        buttonList[6].grid(row=5,column=0)
        buttonList[7].grid(row=5,column=1)
        buttonList[8].grid(row=5,column=2)
        buttonQuit.grid(row=0,column=0)
        winsLossesText.grid(row=0,column=1)
        buttonRestart.grid(row=0, column=2)

    #Changes value of the Button clicked, updates the characterList, locks button, then calls update function
    def btnClicked(self, button):
        print("btnClicked called")
        button['text'] = "x"
        self.updateCharListFromBoard()
        self.lockClickedButton(button)
        self.updateBoard()
            
  
        
    
    def updateBoard(self):
        print("Board Updating")
        
#        #Send characterList to server
#        data = pickle.dumps(self.characterList)
#        mySocket.send(data)
#        
#        #Receive characterList from server
#        self.characterList = pickle.loads(mySocket.recv(4096))
        
        #updates board from character list
        self.updateBoardFromCharList()
        self.lockAllFilledButtons()   
        
        #Checks data received from server for any added win conditions
        #Player won match
        if self.characterList[-1] == 'w':
            self.playerWins += 1
            self.WLText = "W:"+str(self.playerWins)+" L:"+str(self.serverWins)
            self.popUpMsg("You have won the match")
            self.checkGame()
            self.eraseBoard()
        #Server won match
        elif self.characterList[-1] == 'l':
            self.serverWins += 1
            self.WLText = "W:"+str(self.playerWins)+" L:"+str(self.serverWins)
            self.popUpMsg("The computer has won the match")
            self.checkGame()
            self.eraseBoard()
        #Match was a tie
        elif self.characterList[-1] == 't':
            self.popUpMsg("The match was a tie")
            self.eraseBoard()
        

        
        
    #Erases local board and sets win counters to 0
    def restart(self):
        print("restart clicked")
        self.playerWins = 0
        print(self.playerWins)
        self.serverWins = 0
        print(self.serverWins)
        self.WLText = "W:"+str(self.playerWins)+" L:"+str(self.serverWins)
        self.eraseBoard()         
        
    #Should set all board values back to ""     
    def eraseBoard(self):
        print("Erasing board")
        for i in buttonList:
            i['text'] = ""
        self.characterList = self.originalList
        self.enableButtons()
        
        
    #Checks characterList array to see if any buttons need to be locked
    def lockAllFilledButtons(self):
        print("lockAllFilledButtons called")
        index = 0
        for button in buttonList:
            self.lockFilledButton(buttonList[index])
            index += 1
        
    #Locks a button if it has been filled
    def lockFilledButton(self, button):
        print("lockFilledButton called")
        if button['text'] != "":
            button.config(state=tk.DISABLED)
        
    #Disables a single button for when a choice has been made    
    def lockClickedButton(self, button):
        print("LockFilledButton called")
        button.config(state=tk.DISABLED)    
    
    #Disables buttons, for at end of match
    def disableButtons(self):
        print("Buttons disabled")
        for button in buttonList:
            button.config(state=tk.DISABLED)
        
    #Enables buttons, for at start of match
    def enableButtons(self):
        print("Buttons enabled")
        for button in buttonList:
            button.config(state=tk.NORMAL)
         
            
    #updates character list from board values that gets sent to the server
    def updateCharListFromBoard(self):
        print("updateCharFromBoard called")
        index = 0
        for i in buttonList:
            self.characterList[index] = i['text']
            print(self.characterList[index])
            index +=1
            
    #updates board buttons from character list received from server
    def updateBoardFromCharList(self):
        print("updateBoadFromCharList called")
        index = 0
        for i in self.characterList:
            buttonList[index]['text'] = i
            print(self.characterList[index])
            index +=1      
    
        
    #Checks to see if anyone has won the entire game
    def checkGame(self):
        if self.serverWins >= 3:
            self.popUpMsg("You have won the game!")
            
        elif self.playerWins >= 3:
            self.popUpMsg("The computer has won the game!")

    def popUpMsg(self, message):
        popup = tk.Tk()
        popup.wm_title("Win")
        label = ttk.Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ackButton = ttk.Button(popup, text="Okay", command = popup.destroy)
        ackButton.pack()
        popup.mainloop()


#host = '127.0.0.1'
#port = 12345
#mySocket = socket.socket()
#mySocket.connect((host.port))

root = tk.Tk()
root.geometry("360x430")
app = Window(root)
app.mainloop()
#mySocket.close