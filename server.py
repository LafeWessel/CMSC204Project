"""
File contains code for the server side of the Tic Tac Toe program
"""


import socket
import pickle
import random

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

s = socket.socket()
host = "127.0.0.1"
print("Host is: " + host)
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    c.send ('Thank you for connecting'.encode())
    while True:
        receivedList = pickle.loads(c.recv(4096))
        print("They sent us: \"" + receivedList + "\"")
        #ASSUMING THAT EMPTY BUTTONS HAVE EMPTY STRINGS, NOT SPACES
        
        
        #if client wins, append w
        if  didWin("x", receivedList):
            receivedList.append("w")
            #client wins
            
        #if tie, append t
        if didTie(receivedList):
            receivedList.append("t")
        
        else:
            while True:    
                decision = random.randint(0,9)
                if receivedList[decision] == "":
                    receivedList[decision] == "o"
                    break;
            
        #if server wins, append l
        if  didWin("o", receivedList):
            receivedList.append("l")
            
        #if tie, append t
        if didTie(receivedList):
            receivedList.append("t")
            

        c.send (pickle.dumps(receivedList))
