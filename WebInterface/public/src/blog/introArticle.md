This project was completed by
Ruben Schut,
Diarmuid Kelly,
Brown Ogum,
and
Daniel Salamon
for the course Logical Aspects of Multi Agent Systems, 2020.
The goal of this project is to explore how agent beliefs and knowledge in a multi-agent system
behave under the conditions of a game where agents must trust and build knowledge graphs of
each others' knowledge in order to make bets and predict beliefs about the state of the game. 
<div id="intro"></div>

# What is Liar's Dice?

<!--<img src={./src/blog/dice-gif.gif} width="200" height="200"/>-->
<img src={./src/blog/liarsdice.jpg} width="300" height="200" style="border-radius: 8px  "/>
### Setup and initial rules
Liar's Dice is a game of deception. The game is played with at least 2 players with each being given 5 dice in the 'single hand' variant of the game.
The game is played in turn based rounds, where each player rolls their dice concealed from other players under a cup.
A player makes a bet that there is at least *n* number of dice with the face value *x*
under all the concealed cups including their own, for example player one states there are
at least four 3's on the table. The face value 1 is wild and counts towards the count of any higher face value,
so three 3's and one 1 translates to four 3's being a valid bet.

### Making a turn
Moving clockwise around the table each player can either challenge the previous bid,
or increase the bid by stating a higher number of dice with value *x*, or the same 
 quantity *n* and a different face value, *x*, or both a different face value *x* and a higher quantity *n*.
 A bid can be challenged by the player following when the challenger does not believe that the
 statement of *n* dice with *x* value represents what is actually on the table. If the bid is challenged, all players must reveal their dice. The challenger wins if the bidder placed a bid of a higher 
 quantity of dice of value *x* than there are on the table including the 1's in the count.
 If the bidder correctly stated there are at least *n* number of dice then the challenger loses.
 
### Winning conditions
The player that loses the round, either the challenger or the bidder, removes one dice from their
'hand' and starts the next round with the first bid, continuing in the process as described above. 
Once a player loses all their dice, they are removed from the game. The player with at least one remaining
die after all rounds is the winner. 
 
 <img src={./src/blog/Slide1.jpg} width="500" height="400" style="border-radius: 8px; "/>
