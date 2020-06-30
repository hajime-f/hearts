import settings as st
import agent

def main():

    agents = [agent.Agent() for i in range(st.NUM_PR)]

    # making agents playing hearts in NUM_GAMES games
    for i in range(st.NUM_GAMES):
        play_games(agents)


def play_games(agents):

    # initializing card history (which card was discarded in each turn of each trick)
    card_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # initializing agent history (who discarded the card in each turn of each trick)
    agent_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # distributing cards to four agents
    distribute_cards(agents)

    # starting a game
    for trick in range(st.NUM_KC):
        winner = get_winner(card_history[trick-1])
        for turn in range(st.NUM_PR):
            card_history[trick][turn] = 0

    # calculating penalty points of each agent
    penalty_points = calculate_penalty_points(card_history, agent_history)

    # writing the result of the game
    write_result(card_history, agent_history, penalty_points)



def distribute_cards(agents):
    import random
    l = list(range(st.NUM_CARDS))
    dist_cards = random.sample(l, len(l))
    for i in range(st.NUM_PR):
        agents[i].set_cards(dist_cards[i*st.NUM_KC:(i+1)*st.NUM_KC])

def get_winner(history):
    pass

def calculate_penalty_points(card_history, agent_history):
    pass

def write_result(card_history, agent_history, penalty_points):
    pass


if __name__ == '__main__':
    main()
