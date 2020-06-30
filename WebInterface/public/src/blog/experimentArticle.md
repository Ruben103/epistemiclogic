<div id="experiments"></div>

## Experiments
One of the most important skills in Liar Dice is bluffing and capability to challenge biddings in appropriate moment. In our implementation, we decided to model lying and believing by adding two variables, which allow to parameterize those features for every player. Each parameter is a number from 0 to 1, which corresponds to a probability of believing in previous bid or to bluff in the bid of current agent. That brings a big number of possibilities to model different types of players and examine which strategy will provide the highest chance to win the Liar's Dice game. To make use of it, we decided to carry out some interesting experiments with various numbers of players in the game.

### 2 - players game

In case of 2 - players game, we decided to examine different combinations of believing and bluffingparameters  against  a  specific  type  of  opponent.   For  every  set  of  parameters  agents  played  100 games  of  Liar’s  Dice,  as  in  2-players  simulations  the  computacional  and  time  cost  are  easier  tohandle.  To make it clear, all of the experiments are listed below:

<ul>
  <li>Exp 1: Truthful opponent - Believing parameter value: 1.0 | Lying parameter value: 0.0 </li>
  <li>Exp 2: Complete liar - Believing parameter value: Random | Lying parameter value: 1.0</li>
  <li>Exp 3: Disbeliever - Believing parameter value: 0.0 | Lying parameter value: Random</li>
  <li>Exp 4: Average opponent - Believing parameter value: 0.5 | Lying parameter value: 0.5</li>
  <li>Exp 5: Random opponent - Believing parameter value: Random | Lying parameter value: Random</li>
</ul>



<img src={WebInterface/public/Thruthful_Opponent_1.png} width="500" height="300" style="border-radius: 8px  "/>
