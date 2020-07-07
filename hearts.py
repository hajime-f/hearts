import os, sys, datetime, random
import settings as st
import common as cm
import random_agent, rule_based_agent

def main():

    # assigning agents
    # 1 -> random_agent, 2 -> rule_based_agent,
    ind = [2, 1, 1, 1]

    # creating instances of agents
    agents = [0] * st.NUM_PR
    for i in range(st.NUM_PR):
        if ind[i] == 1:
            agents[i] = random_agent.Random_agent()
        elif ind[i] == 2:
            agents[i] = rule_based_agent.Rule_based_agent()

    # creating a directory for writing log
    dt_now = datetime.datetime.now()
    dir_name = dt_now.strftime('%Y%m%d_%H%M%S')
    try:
        os.makedirs(dir_name)
    except FileExistsError:
        sys.exit('The directory exists.')

    # making agents playing the card game "Hearts" in NUM_GAMES games
    for i in range(st.NUM_GAMES):
        penalty_points = play_game(agents, i, dir_name)
        write_penalty_log(penalty_points, dir_name)


def play_game(agents, game_number, dir_name):

    # initializing card history (which card was discarded in each turn of each trick)
    card_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # initializing agent history (who discarded the card in each turn of each trick)
    agent_history = [[-1 for j in range(st.NUM_PR)] for i in range(st.NUM_KC)]

    # initializing heart break flog
    hb_flag = 0

    # distributing cards to four agents
    dist_cards = distribute_cards(agents)

    # Getting the playing sequence in the first trick based on their hands
    # (the agent who has C-2 is the leading player in the initial trick)
    winner = dist_cards.index(0) // st.NUM_KC

    # starting a game
    for trick in range(st.NUM_KC):
        seq = cm.get_agent_sequence(winner)
        for turn, j in zip(range(st.NUM_PR), seq):
            selected_card = agents[j].select_card(card_history, agent_history, trick, turn)
            if not hb_flag and selected_card >= st.H_2:
                hb_flag = heart_break(agents)
            if selected_card == -1:
                write_playing_log(card_history, agent_history, dist_cards, game_number, [0 for i in range(st.NUM_PR)], dir_name)
                sys.exit('A wrong card is selected in game #' + str(game_number+1))
            else:
                card_history[trick][turn] = selected_card
                agent_history[trick][turn] = j
        winner = cm.get_winner(card_history[trick], agent_history[trick])
        if winner == -1:
            sys.exit('A wrong winner is selected')

    # calculating penalty points
    penalty_points = calculate_penalty_points(card_history, agent_history)

    # writing playing log
    if st.DEBUG_MODE:
        write_playing_log(card_history, agent_history, dist_cards, game_number, penalty_points, dir_name)

    # closing the game
    for a in agents:
        a.end_game()
    del card_history, agent_history, dist_cards, seq

    return penalty_points

def distribute_cards(agents):
    while True:
        l = list(range(st.NUM_CARDS))
        dist_cards = random.sample(l, len(l))
        if not is_all_heart(dist_cards):
            break
    for i in range(st.NUM_PR):
        agents[i].set_cards(dist_cards[i*st.NUM_KC:(i+1)*st.NUM_KC])
    del l
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

def heart_break(agents):
    for a in agents:
        a.hb_flag = 1
    return 1

def calculate_penalty_points(card_history, agent_history):
    penalty_points = [0] * st.NUM_PR
    for card_seq, agent_seq in zip(card_history, agent_history):
        penalty = 0
        for card in card_seq:
            if card >= st.H_2:
                penalty += 1
            elif card == st.S_Q:
                penalty += 13
            else:
                pass
        penalty_points[cm.get_winner(card_seq, agent_seq)] += penalty
    return penalty_points

def write_playing_log(card_history, agent_history, dist_cards, game_number, penalty_points, dir_name):

    f = open(dir_name+'/log_'+str(game_number+1).zfill(6)+'.log', mode='w')
    hand_list = [[-1 for j in range(st.NUM_KC)] for i in range(st.NUM_PR)]
    for j in range(st.NUM_PR):
        hand_list[j] = dist_cards[j*st.NUM_KC:(j+1)*st.NUM_KC].copy()
        hand_list[j].sort()
        hand_str = 'Agent ' + str(j+1) + ': '
        for i in hand_list[j]:
            hand_str += str(st.CARD_NAME[i]) + ', '
        hand_str += '\n'
        f.write(hand_str)
    f.write('\n')

    for card_seq, agent_seq, trick in zip(card_history, agent_history, range(st.NUM_KC)):
        f.write('==== Trick ' + str(trick+1) + ' ====\n')
        for card, agent, turn in zip(card_seq, agent_seq, range(st.NUM_PR)):
            f.write('Agent ' + str(agent+1) + ': ' + str(st.CARD_NAME[card]))
            try:
                hand_list[agent].remove(card)
            except ValueError:
                print('ValueError: hearts.py in line 146')
                sys.exit(card_history)
            hand_str = ' -> '
            for i in hand_list[agent]:
                hand_str += str(st.CARD_NAME[i]) + ', '
            f.write(hand_str + '\n')

    f.write('==================\n')

    for i in range(st.NUM_PR):
        f.write('Agent ' + str(i+1) + ': ' + str(penalty_points[i]) + '\n')

    del hand_list
    f.close()
    return 1

def write_penalty_log(penalty_points, dir_name):
    with open(dir_name+'/'+st.FILE_NAME, mode='a') as f:
        for p in penalty_points:
            f.write(str(p)+', ')
        f.write('\n')

if __name__ == '__main__':
    main()
