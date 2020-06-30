import random
import settings as st
#import agent

def play_games(agents):

    # initializing card history (which card was discarded in each turn of each trick)
    card_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # initializing agent history (who discarded the card in each turn of each trick)
    agent_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # distributing cards to four agents
    l = list(range(st.NUM_CARDS))
    dist_cards = random.sample(l, len(l))
    for i in range(st.NUM_PR):
        agents[i].set_cards(dist_cards[i*st.NUM_KC:(i+1)*st.NUM_KC])

    for trick in range(st.NUM_KC):
        winner = get_winner(card_history[trick-1])
        for turn in range(st.NUM_PR):
            card_history[trick][turn] = 0 #

def main():

#    agents = [Agent() for i in range(st.NUM_PR)]

    # making agents playing hearts in NUM_GAMES games
    for i in range(st.NUM_GAMES):
        play_games(agents)


if __name__ == '__main__':
    main()
