# Liar's Dice
### Ruben Schut, Diarmuid Kelly, Daniel Salamon, Brown Ogum

-----
This program exectutes one iteration of the game of liar's dice that we've developed for the course Logical
Aspects of Multi-Agent system. The program takes no input. The default number of players is 4 and the default number of dice is 6.

There are three main classes

Game - Responsible for the flow of the game and its history

Round - Controls the flow of one round. Keeps track of bids and valuations

Player - Asks each player for bids. Players have Believing and Lying parameters

Refer for more information to: https://ruben103.github.io/epistemiclogic/
 

##Run Instructions
Please make sure Numpy is on your machine. Consider a virtual machine
<br/>Command to execute the program: ```python3 main.py```

####Install Virtual Environment
Run the following commands in sequence (in linux add ```sudo```):
<br/>```pip3 install virtualenv```
<br/>```virtualenv venv```
<br/>```source venv/bin/activate```
<br/>```pip3 install -r requirements.txt```
<br/> This will ensure the keras and tensorflow requirements are stable.

