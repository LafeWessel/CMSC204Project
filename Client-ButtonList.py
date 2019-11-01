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

    Add locking of buttons when filled
    
"""

#Imports and initialization of tkinter object
import tkinter as tk
import pickle
import socket

buttonList = []


class Window(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.characterList = ["","","","","","","","",""]
        self.master = master
        self.initWindow()
        self.numberOfGames = 5
        self.playerWins = 0
        self.serverWins = 0
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
        self.pack()
        hght = 6
        wdth = 12
        
        buttonList.append(tk.Button(self, text=self.characterList[0], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[0])))
        buttonList.append(tk.Button(self, text=self.characterList[1], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[1])))
        buttonList.append(tk.Button(self, text=self.characterList[2], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[2])))
        buttonList.append(tk.Button(self, text=self.characterList[3], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[3])))
        buttonList.append(tk.Button(self, text=self.characterList[4], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[4])))
        buttonList.append(tk.Button(self, text=self.characterList[5], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[5])))
        buttonList.append(tk.Button(self, text=self.characterList[6], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[6])))
        buttonList.append(tk.Button(self, text=self.characterList[7], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[7])))
        buttonList.append(tk.Button(self, text=self.characterList[8], height=hght, width=wdth, command=lambda: self.btnClicked(buttonList[8])))

        print(buttonList)
        buttonQuit = tk.Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = tk.Button(self, text = "Restart",command=lambda: self.restart())
        
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
        buttonRestart.grid(row=0, column=2)
        

    #should change the value of the empty button to be the player's and then tell the server what changed
    def btnClicked(self, i):
        i['text'] = "x"
        self.updateCharList()
            
    #Erases local board
    def restart(self):
        print("restart clicked")
        self.eraseBoard()   
        
    #TODO sends and receives data to and from server
    def updateBoard(self):
        
        
        #send character list with pickle
        #data = pickle.dumps(self.characterList)
        #mySocket.send(data)
        
        #Receive characterList
        #characterList = pickle.loads(c.recv(4096))
        
        #updates board from character list
        self.updateBoardFromCharList()
        print("Board Updating")
        
        
        
    #Should set all board values back to " "     
    def eraseBoard(self):
        print("Erasing board")
        for i in buttonList:
            i['text'] = ""
        self.characterList = []
        self.updateCharList()
        self.enableButtons()
        
    
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
            
    #updates character list that gets sent to the server
    def updateCharList(self):
        index = 0
        for i in buttonList:
            self.characterList[index] = i['text']
            print(self.characterList[index])
            index +=1
            
    #updates buttons from character list received from server
    def updateBoardFromCharList(self):
        index = 0
        for i in self.characterList:
            buttonList[index]['text'] = i
            print(self.characterList[index])
            index +=1       
    
    def playerWin(self):
        self.playerWins += 1
        print("Player has won: ", self.playerWins)
        self.eraseBoard()

    def serverWin(self):
        self.serverWins += 1
        print("Server has won: ", self.serverWins)
        self.eraseBoard()
        
    #Checks to see if anyone has won the entire game
    def checkGame(self):
        if self.serverWins >= 3:
            self.endPopUp("You")
            
        elif self.playerWins >= 3:
            self.endPopUp("The Computer")
            
    #TODO Add popup
    def endPopUp(self, name):
        print("%s has won!", name)
        

        
#global buttonValues = [" "," "," "," "," "," "," "," "," "]

root = tk.Tk()
root.geometry("400x350")
app = Window(root)
app.mainloop()