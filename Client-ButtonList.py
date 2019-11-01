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
"""




#Imports and initialization of tkinter object
from tkinter import *

buttonList = []

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.initWindow()
    
    #creates and lays out buttons
    def initWindow(self):
        
        self.master.title("Tic Tac Toe")
        self.pack()
        
        buttonList.append(Button(self, text=0, height=6, width=12, command=lambda: self.btnClicked(buttonList[0])))
        buttonList.append(Button(self, text=1, height=6, width=12, command=lambda: self.btnClicked(buttonList[1])))
        buttonList.append(Button(self, text=2, height=6, width=12, command=lambda: self.btnClicked(buttonList[2])))
        buttonList.append(Button(self, text=3, height=6, width=12, command=lambda: self.btnClicked(buttonList[3])))
        buttonList.append(Button(self, text=4, height=6, width=12, command=lambda: self.btnClicked(buttonList[4])))
        buttonList.append(Button(self, text=5, height=6, width=12, command=lambda: self.btnClicked(buttonList[5])))
        buttonList.append(Button(self, text=6, height=6, width=12, command=lambda: self.btnClicked(buttonList[6])))
        buttonList.append(Button(self, text=7, height=6, width=12, command=lambda: self.btnClicked(buttonList[7])))
        buttonList.append(Button(self, text=8, height=6, width=12, command=lambda: self.btnClicked(buttonList[8])))

        print(buttonList)
        buttonQuit = Button(self, text="Quit",command=self.master.destroy)
        buttonRestart = Button(self, text = "Restart",command=lambda: self.restart())
        
        
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
        
        #This keeps the user from inputting any data until the server gives it permission to
        #self.disableButtons()
        #self.eraseBoard()
        self.updateBoard
    #should change the value of the empty button to be the player's and then tell the server what changed
    def btnClicked(window, i):
        i['text'] = "x"
        #If the spot is not take, it will assign the new value and update the board, otherwise nothing happens
        
            
    #Erases local board and tells server to delete memory and begin a new instance of the game
    def restart(button):
        print("restart clicked")
        eraseBoard()        
        
    #Sets the boards values to whatever is in the buttonValues list
    def updateBoard(self):
        
        print("Board Updating")  
        
    #Should set all board values back to " "     
    def eraseBoard(self):
        print("Erasing board")
        for i in buttonList:
            i['text'] = ""
        
    #Sends choice back to server
    def submitChoice(choiceLocation):
        print("Choice Submitted")
    
    
    #Disables buttons, for at end of match
    def disableButtons(self):
        print("Buttons disabled")
        for button in buttonList:
            button.config(state=DISABLED)
            print("%s was disabled",button)
        
    #Enables buttons, for at start of match
    def enableButtons():
        print("Buttons enabled")
        for button in buttonList:
            button.config(state="normal")


        

        
#global buttonValues = [" "," "," "," "," "," "," "," "," "]

root = Tk()
root.geometry("400x350")
app = Window(root)
app.mainloop()