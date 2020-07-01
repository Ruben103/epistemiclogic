<div id="conclusions"></div>

# Conclusions
According  to  the  results  of  our  experiments,  we  can  conclude  that  believing  parameter  playedsignificant role in the simulations.  There is almost a linear dependency 
between its amount andnumber of games our agent managed to win.  According to that correlation, we can easily deducethat believing in others players bids is an optimal strategy, 
no matter of which strategy the opponentwill choose.  That is compatible with our intuition.  Calling a lie is a bit risky in Liar’s Dice, sincewe have to have quite a lot of 
knowledge about dices in the game.  Therefore it might be better to try overbid the previous player. 
  Some of results obtained from experiments with 2 contestants are surprising.  
For example, it is still better to believe in our opponent bids, when we are playing against a liar.  Furthermore, itcame out that the most difficult opponent is the one who 
believes in every bid we make and neverlie - our agent won 56% of games played against him.  In case, when our opponent never believes inour bids, the frequency of our false bets 
can be any.  No matter what we say, our rival will alwayscall a lie,  which,  as the results indicates,  is the worst strategy.  In case when parameters of theopponent were 
randomized, our agent was won 83/100 games with lying parameter set to 0.8.
  In case of Liar’s Dice with more than 2 players, results are also quite interesting.  The strategyof 
believing in every bid still guarantee the highest probability of winning the game.  With that setting, according to the number of opponents, our agent was able to win:

<ul>
  <li> 66/100 games with lying parameter value = 0.7, and $\approx$ 60\% of games overall against 2 opponents, </li>
  <li> 56/100 games with lying parameter values = \{0.5, 0.3\} and $\approx$ 52\% of games overall against 3 opponents, </li>
  <li> 52/100 games with lying parameter value = 0.3, and $\approx$ 46\% of games overall against 4 opponents. </li>
</ul>

The following histogram shows the results described above, taking into account also the outcome of game with one opponent:


<img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/histogram.png} width="700" height="500" style="border-radius: 8px; align: center;"/>

That leads to some instructive conclusions. Firstly, when number of players in the game increases, it becomes harder to win. Secondly, it is better to lie less, when we play 
against more opponents.

To summarize, results from our experiments indicates, that believing in every bid and lying in around half of our turns (depending on the number of competitors) is the optimal 
strategy in our multi-agent system, when we have not any knowledge about our opponents preferences.
