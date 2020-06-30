<div id="experiments"></div>

## Experiments
One of the most important skills in Liar Dice is bluffing and capability to challenge biddings in appropriate moment. In our implementation, we decided to model lying and believing by adding two variables, which allow to parameterize those features for every player. Each parameter is a number from 0 to 1, which corresponds to a probability of believing in previous bid or to bluff in the bid of current agent. That brings a big number of possibilities to model different types of players and examine which strategy will provide the highest chance to win the Liar's Dice game. To make use of it, we decided to carry out some interesting experiments with various numbers of players in the game.

### 2 - players game

In case of 2 - players game, we decided to examine different combinations of believing and bluffingparameters  against  a  specific  type  of  opponent.   For  every  set  of  parameters  agents  played  100 games  of  Liar’s  Dice,  as  in  2-players  simulations  the  computacional  and  time  cost  are  easier  tohandle.  To make it clear, all of the experiments are listed below:

<ul>
  <li>Exp 1: Truthful opponent - Believing parameter value: <b>1.0</b> | Lying parameter value: <b>0.0</b> </li>
  <li>Exp 2: Complete liar - Believing parameter value: <b>Random</b> | Lying parameter value: <b>1.0</b></li>
  <li>Exp 3: Disbeliever - Believing parameter value: <b>0.0</b> | Lying parameter value: <b>Random</b></li>
  <li>Exp 4: Average opponent - Believing parameter value: <b>0.5</b> | Lying parameter value: <b>0.5</b></li>
  <li>Exp 5: Random opponent - Believing parameter value: <b>Random</b> | Lying parameter value: <b>Random</b></li>
</ul>

Results of each experiment mentiond above are shown in the following figures:
<div class="row">
    <div class="column">
      <img src={WebInterface/public/Thruthful_Opponent_1.png} width="500" height="400" style="border-radius: 8px  " caption="xd" style="vertical-align:middle;"/>
      <img src={WebInterface/public/Disbeliever_3.png} width="500" height="400" style="border-radius: 8px  " style="vertical-align:middle;"/>
    </div>
    <div class="column">
      <img src={WebInterface/public/Liar_2.png} width="500" height="400" style="border-radius: 8px  " style="vertical-align:middle;"/>
      <img src={WebInterface/public/Average_Opponent_4.png} width="500" height="400" style="border-radius: 8px  " style="vertical-align:middle;"/>
      <img src={WebInterface/public/Random_5.png} width="500" height="400" style="border-radius: 8px  " style="vertical-align:middle;"/>

    </div>

</div>



