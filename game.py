from datetime import datetime as dt
import settings as st
import os, random

class Game():
    
    def __init__(self, agents):
        
        self.agents = agents
        self.dir_name = dt.now().strftime('%Y%m%d_%H%M%S')
        
        try:
            os.makedirs(self.dir_name)
        except FileExistsError:
            exit('The directory exists.')
            
        
    def play_games(self):
        
        # making agents playing the card game "Hearts" in NUM_GAMES games
        for i in range(st.NUM_GAMES):
            penalty_points = self.play_one_game()
            

    def play_one_game(self):

        # initializing game settings
        hb_flag = 0
        card_history, agent_history = self.initialize_history()

        # distributing cards to four agents
        dist_cards = distribute_cards()
        
        # Getting the playing sequence in the first trick based on their hands
        # (the agent who has C-2 is the leading player in the initial trick)
        winner = dist_cards.index(0) // st.NUM_KC

        # starting a game
        for trick in range(st.NUM_KC):
            seq = cm.get_agent_sequence(winner)
            for turn, j in enumerate(seq):
                selected_card = agents[j].select_card(card_history, agent_history, trick, turn)
                if not hb_flag and selected_card >= st.H_2:
                    hb_flag = heart_break(agents)
                if selected_card == -1:
                    print(agents[j])
                    write_playing_log(card_history, agent_history, dist_cards, game_number, [0 for i in range(st.NUM_PR)], dir_name)
                    sys.exit('A wrong card is selected in game #' + str(game_number+1))
                else:
                    card_history[trick][turn] = selected_card
                    agent_history[trick][turn] = j
            winner = cm.get_winner(card_history[trick], agent_history[trick])
            if winner == -1:
                sys.exit('A wrong winner is selected')
        


    def initialize_history(self):

        card_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]
        agent_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

        return card_history, agent_history
    
    
    def distribute_cards(self):
        
        while True:
            l = list(range(st.NUM_CARDS))
            dist_cards = random.sample(l, len(l))
            if not self.is_all_heart(dist_cards):
                break
        for i in range(st.NUM_PR):
            self.agents[i].set_cards(dist_cards[i * st.NUM_KC : (i+1) * st.NUM_KC])
            
        return dist_cards
            

    def is_all_heart(dist_cards):
        
        for j in range(st.NUM_PR):
            k = 0
            for i in range(st.NUM_KC):
                if dist_cards[st.NUM_KC * j + i] < st.H_2:
                    break
                else:
                    k += 1
            if k == st.NUM_KC:
                return 1
        return 0
                
    
