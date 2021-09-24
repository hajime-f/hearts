import settings as st
from random_agent import RandomAgent
from rule_based_agent import RuleBasedAgent
from game import Game

if __name__ == '__main__':

    # assigning agents
    # 1 -> Random agent
    # 2 -> Rule-based agent
    idx = [2, 1, 1, 1]

    # creating instances of agents
    agents = []
    for i in range(st.NUM_PR):
        if idx[i] == 1:
            agents.append(RandomAgent())
        elif idx[i] == 2:
            agents.append(RuleBasedAgent())
        else:
            exit('A wrong number is selected.')
            

    game = Game(agents)
            
    # making agents playing the card game "Hearts" in NUM_GAMES games
    for i in range(st.NUM_GAMES):
        penalty_points = play_game(agents, i, dir_name)
        write_penalty_log(penalty_points, dir_name)
    
