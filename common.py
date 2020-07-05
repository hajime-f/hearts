import settings as st

def get_suit(card):
    return card // st.NUM_KC

def is_card_in_hand(hand, card):
    for h in hand:
        if h == card:
            return 1
    return 0

def is_suit_in_hand(hand, card):
    suit = get_suit(card)
    for h in hand:
        if h != -1 and suit == get_suit(h):
            return 1
    return 0

def is_not_heart_in_hand(hand):
    for h in hand:
        if h != -1 and get_suit(h) != st.HEART:
            return 1
    return 0

def get_winner(card_seq, agent_seq):
    leading_card = card_seq[0]
    if leading_card == -1:
        print('Leading card is wrong.')
    else:
        lc_suit = get_suit(leading_card)
        winner = agent_seq[0]
        for h, a in zip(card_seq, agent_seq):
            if lc_suit == get_suit(h) and leading_card < h:
                leading_card = h
                winner = a
        return winner
    return -1

def get_agent_sequence(winner):
    seq = []
    for i in range(st.NUM_PR):
        if winner+i < st.NUM_PR:
            seq.append(winner+i)
        else:
            seq.append(winner+i-st.NUM_PR)
    return seq
