# Liar's Dice - Project for Epistemic Logic
[Modify this file for the website/paper](WebInterface/public/src/blog/mainArticle.md)

[Temporary website location](https://diarmuidkelly.github.io/epistemiclogic/)

The code is structured as follows:<br/>
There are three classes: Game(), Round() and Player()

The Game() controls the overall sequence of rounds. It contains players and rounds

Round() controls the overall sequence of biddings and valuations. It contains players, but can also access parent class Game()

Player() contains knowledge bases, valuation functions, dice amounts, current bids etc..

---

First, to run the code execute:<br/> pip install --upgrade pip; pip3 install -r requirements.txt<br/>
 to install the dependencies for this program