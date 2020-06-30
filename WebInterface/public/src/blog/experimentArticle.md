<div id="experiments"></div>

# Experiments
One of the most important skills in Liar Dice is bluffing and capability to challenge biddings in appropriate moment. In our implementation, we decided to model lying and believing by adding two variables, which allow to parameterize those features for every player. Each parameter is a number from 0 to 1, which corresponds to a probability of believing in previous bid or to bluff in the bid of current agent. That brings a big number of possibilities to model different types of players and examine which strategy will provide the highest chance to win the Liar's Dice game. To make use of it, we decided to carry out some interesting experiments with various numbers of players in the game.

## 2 - players game

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
      <h3> Exp 1: Thruthful Opponent </h3>
        <img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/Thruthful_Opponent_1.png} width="700" height="500" style="border-radius: 8px  " caption="xd" style="vertical-align:middle;"/>
    </div>
    <div>
      <h3> Exp 2: Complete liar </h3>
      <img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/Liar_2.png} width="700" height="500" style="border-radius: 8px  " style="vertical-align:middle;"/>
    </div>
    <div>
      <h3> Exp 3: Disbeliever </h3>
      <img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/Disbeliever_3.png} width="700" height="500" style="border-radius: 8px  " style="vertical-align:middle;"/>
    </div>
    <div class="column">
      <h3> Exp 4: Average Opponent </h3>
      <img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/Average_Opponent_4.png} width="700" height="500" style="border-radius: 8px  " style="vertical-align:middle;"/>
    </div>
    <div>
      <h3> Exp 5: Random Opponent </h3>
      <img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/Random_5.png} width="700" height="500" style="border-radius: 8px  " style="vertical-align:middle;"/>
    </div>
    

</div>

## 3 and more players game

When we have been performing experiments with 2 players, we have made some assumptions about the opponent, for example, that he is always trying to bluff or that he believe that every bid we make is truthful. In the real world, we can make such an assumptions about our opponents only after several rounds played. It is worth to notice, that in our environment, agents do not have any knowledge about their opponents strategies. Therefore, in further experiments, we have assigned random values for believing and lying parameters for every opponent in 3, 4 and 5 - players game. That brought us a broader view on which parameters are more "universal" - that means which parameters performs better, when the distribution of opponents is differential. To make the simulations in a reasonable time, we reduced the number of dices from 6 to 4 for each agent. Plots from experiments are shown below:

### 3-players 

<img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/3_players_two_random.png} width="700" height="500" style="border-radius: 8px  " style="display: block;margin-left: auto;margin-right: auto;width: 60%;"/>

### 4-players

<img src={https://raw.githubusercontent.com/Ruben103/epistemiclogic/master/WebInterface/public/images/4_players.png} width="700" height="500" style="border-radius: 8px  " style="vertical-align:middle;"/>

### 5-players

