# CMSC204Project
CMSC 204 Protocol Design Project - Tic Tac Toe
Lafe, Brandon, Joel, Ian

# 1 Page Hand-in
The connecting client makes the first move shown on the GUI and sends the move to the server as a list of characters. When the server is making its move, all of the buttons are locked so that the client can not make any moves. Any buttons that have an X or an O on them are locked so that they cannot be chosen again. When the server receives the list of characters, it determines whether the client has won, the server has won, or the match is a tie. If one of these has occurred, a unique character is appended to the end of the list that is then sent back to the client. If none of these have occurred, the server then uses a random number generator to determine a random spot, and if that spot is free, then it places an O there. Else, it continues until it finds a free spot. It then sends back an updated list of characters that the client uses to update its own list, board, and GUI. The client then reads the last character of the returned list, and if it has one of the special characters used to signify a win or tie, it updates the label if needed and clears the board for the next game. However, if the server or client has won 3 matches, then it shows a pop-up message saying who has won the game.
When the client is ready to send the character list to the server, it uses the pickle package to dump the character list and send it to the server. After the client sends the character list, the client waits to receive something back from the server before continuing. The server loads in the character list with pickle. In order to send the character list back, the server dumps and sends the character list with pickle. The server also has to wait for a response from the client to send back a character list. The client receives back the updated character list and continues on. The client is thick and the server is thin. The server only determines the winner or a tie for the match and makes a random move from the given board. Most of the program lies in the client with the GUI.

# Instructions for use
- Run the server.py file on any given machine.
- Run the client.py file on another machine, typing in the server's IP address in the console will allow a connection to be made between the two devices.
- Play the game by attempting to make 3-in-a-row
- 'Restart' will clear the board and the total wins and losses
- 'Quit' will close the process and tell the server to close its processes
- The game is best of 3 matches, which are tallied in the top-center text box
