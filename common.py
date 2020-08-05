import sys
import settings as st

def get_suit(card):
    return card // st.NUM_KC

def is_card_in_hand(hand, card):
    try:
        return hand.index(card)
    except ValueError:
        return -1
#    for h in hand:
#        if h == card:
#            return 1
#    return 0

def is_card_discarded_in_game(card_history, card):
    for trick in range(st.NUM_KC):
        if is_card_discarded(card_history[trick], card):
            return 1
    return 0

def is_card_discarded(card_seq, card):
    for c in card_seq:
        if c == -1:
            break
        elif c == card:
            return 1
    return 0

def is_stronger_card_discarded(card_seq, card):
    suit = get_suit(card)
    for c in range(card, st.NUM_KC*(suit+1)):
        if is_card_discarded(card_seq, c):
            return 1
    return 0

def get_remaining_stronger_card_number(card_history, card):
    num = 0
    suit = get_suit(card)
    min_n = suit*st.NUM_KC
    max_n = (suit+1)*st.NUM_KC
    for trick in range(st.NUM_KC):
        for turn in range(st.NUM_PR):
            dist_card = card_history[trick][turn]
            if min_n < dist_card and dist_card < max_n and card < dist_card:
                num += 1
    return num

def get_discarded_suit_number(card_history, suit):
    num = 0
    for trick in range(st.NUM_KC):
        for card in card_history[trick]:
            if suit == get_suit(card):
                num += 1
    return num

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
        sys.exit('The leading card is wrong.')
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
