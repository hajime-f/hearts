import settings as st
from agents.random_agent import RandomAgent
# from rule_based_agent import RuleBasedAgent
from game import Game

if __name__ == '__main__':

    # assigning agents
    # 1 -> Random agent
    # 2 -> Rule-based agent
    idx = [1, 1, 1, 1]

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
    total_penalty_points = game.play_games()
    
