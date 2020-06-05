# Main Article for Epist. Logic

#### June 4, 2020 by [Diarmuid](/)

We would like to do our final research project on a game called Liar’s Dice.  Thegame has many different variations, but the key concept is the following.  Thegame is played using a set of dice.  Each player receives up-front six fair dice.Each round there is at least one loser, who then has to lay away one of his diceleaving him with one less.  The game is over when one person loses his last die.At the start of the game, the person rolls his remaining dice and is allowedto view them.  Note that each player only knows his own dice and not thoseof his/her opponents.  The game is about the beliefs each player has about thedistribution of the dice using the dice of all of the players.  A player needs tomake a claim about this distribution (for instance:  ”I believe there areat leastsix four’son the table”.  The next player needs to overbid the previous bidding.This can be done by increasing either thequantity(in this case six) or thevalue(in this case four).  See example 1.


### Example 1:
There are four players in the game, each holding three dice.The  distribution  is  as  follows: D={(1,2,2),(1,1,3),(3,5,6),(4,3,6)}.   The starting player of the round opens his bidding and says”Two two’s”.  The next player has two choices: raise the value or the quantity. The player chooses to say ”Three two’s”, which means he has overbid the quantity.
### Example 2:
Marie has just made the bidding ”Two sixes”. John is the only allowed to increase the quantity, because no eyes are higher than six.  Johnis then allowed to say ”Three three’s,  he does not have to say ”Three Sixes”. When the quantity is increased, the value may be ’reset’.  NOTE: John is also allowed to skip quantities: he could have immediately went from three to seven.

## End of the game

This continues until a player does not believe a bidding is a proper representation  of  the  distribution  of  the  total  dice  on  the  table. He then  makes  theclaim that he does not believe the statement to be true and challenges the last bidding. The remaining players,  other  than the one who made the  final  bid-ding,  must  also  make  a  claim  whether  they  believe  the  final  bidding  to  be  aproper  representation.   When  everyone  has  made  their  stakes,  all  of  the  dice will become known and the last bidding will be checked. All of those who made the correct claim will not lose a die, all of those who made the incorrect claim will lose a die.
## The pick die

One final adjustment to the probabilities of this game is the fact that the diewith one eye on it will be the Pick die.  This means that upon evaluation of the game, all of the dice with one eye on them also count towards the number of dice of the value that was chosen during the last bidding.  The players in thegame need to incorporate the chance of rolling a one into their biddings as well.

## One final rule

The pick die may be used as an alternative to raising the quantity or the value. A player may opt to make an assumption that there are at least n many pick die on the table.  Notice that the benefit of incorporating the pick die in evaluation is lost when this strategy is chosen.  The rule-of-thumb is that the pick die isalways worth twice the quantity of that of regular dice + a little extra.  This means that if the previous bidding had a quantity of four, the player is allowed to make a bidding of ”Two pick”. The other way around, if two pick dice was the previous bidding, the player needs to have at least a quantity of five(because of the little extra).
Cras mattis consectetur purus sit amet fermentum. Sed posuere consectetur est at lobortis.
## Theoretical Justification

We believe this game is a nice representation of game theory and bridges well between Public Announcement Logic (PAL) and Common Knowledge (C). Each round consists of several biddings that are higher than the previous one.  This means that all of the agents publicly receive information about what the otherplayer’s beliefs are about the distribution of dice.  PAL does not permit an agentto lie about his beliefs about the dice. Therefore, we will build a module that isable to deceive if that agent thinks its his best move.  The biddings will alwaysbe  a  rational  construct  of  the  common  knowledge  pool  and  each  agents  owndice, adjusted for with probabilities. Despite missing this aspect of the game,we still believe it’s interesting to formalise the choices that our agents will makein particular game settings.
