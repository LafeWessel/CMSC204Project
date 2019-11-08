"""
File contains code for the server side of the Tic Tac Toe program
"""

import socket
import pickle
import random
import sys

s = socket.socket()
host = "10.194.7.55"
print("Host is: " + host)
port = 12345
s.bind((host, port))
s.listen(5)
        

try:
    def didWin(player, board):
        #horizontal wins
        if board[0] == player and board[1] == player and board[2] == player:
            return True
        elif board[3] == player and board[4] == player and board[5] == player:
            return True
        elif board[6] == player and board[7] == player and board[8] == player:
            return True
        #vertical wins
        elif board[0] == player and board[3] == player and board[6] == player:
            return True
        elif board[1] == player and board[4] == player and board[7] == player:
            return True
        elif board[2] == player and board[5] == player and board[8] == player:
            return True
        #diagonal wins
        elif board[0] == player and board[4] == player and board[8] == player:
            return True
        elif board[2] == player and board[4] == player and board[6] == player:
            return True
        
        return False
    
    def didTie(board):
        for i in receivedList:
            if i == "":
                return False
            
        return True
    
    receivedList = ["","","","","","","","",""]
    while True:
        c, addr = s.accept()
        print ('Got connection from', addr)
        while True:
            
            receivedList = pickle.loads(c.recv(8192))
           # print("They sent us: \"" + receivedList + "\"")
            #ASSUMING THAT EMPTY BUTTONS HAVE EMPTY STRINGS, NOT SPACES
            print("received something", receivedList)
            
            if (receivedList[0] == "q"):
                print("Client ended game")
                sys.exit()
            
            #if client wins, append w
            if  didWin("x", receivedList):
                receivedList.append("w")
                #client wins
                
            #if tie, append t
            if didTie(receivedList) and receivedList[-1] != "w":
                receivedList.append("t")
            
            elif receivedList[-1] != "w":
                while True:    
                    print("In while loop")
                    decision = random.randint(0,8)
                    print("decision = ", decision)
                    if receivedList[decision] == "":
                        receivedList[decision] = "o"
                        print("receivedList[decision] = ", receivedList[decision])
                        break;
                
            #if server wins, append l
            if  didWin("o", receivedList) and receivedList[-1] != "w" and receivedList[-1] != "t":
                receivedList.append("l")
                
            #if tie, append t
            if didTie(receivedList) and receivedList[-1] != "w" and receivedList[-1] != "t" and receivedList[-1] != "l":
                receivedList.append("t")
                
            print("sending", receivedList)
            stuffToSend = pickle.dumps(receivedList)
            c.send (stuffToSend)
            print("Packet sent")
except EOFError:
    print("A fatal error occured (EOFError)")
    sys.exit()
except ConnectionResetError:
    print("A fatal error occured (ConnectionResetError)")
    sys.exit()
except SystemExit:
    print("Shutting down")