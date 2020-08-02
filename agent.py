import abc
import settings as st
import common as cm

class Agent(metaclass = abc.ABCMeta):

    hand = []
    hb_flag = 0

    def __init__(self):
        pass

    def set_cards(self, cards):
        self.hand = cards.copy()

    def end_game(self):
        del self.hand
        self.hb_flag = 0

    @abc.abstractmethod
    def select_card(self, card_history, agent_history, trick, turn):
        pass

    def validate_card(self, card, card_seq, trick, turn):

        if trick == 0:
            # In the first trick, discarding S-Q is not allowed.
            if card == st.S_Q:
                return 0
            # In the first trick, discarding heart cards is not allowed.
            elif card >= st.H_2:
                return 0
            # In the first turn of the first trick, C-2 must be discarded.
            elif turn == 0:
                if card != st.C_2:
                    return 0
                else:
                    return 1

        print('d')

        if turn == 0:
            # In the first turn, when the heart break has occured, any card cab be discarded.
            if self.hb_flag:
                return 1
            else:
                # Any card except for heart can be discarded in the first turn.
                if cm.get_suit(card) != st.HEART:
                    return 1
                # Even if the heart break has not occured, when the agent has cards whose suit are heart,
                # the cards can be discarded in the first turn.
                elif not cm.is_not_heart_in_hand(self.hand):
                    return 1
                else:
                    return 0

        leading_card = card_seq[0]

        # If the agent has a card whose suit is the same as that of the leading card,
        # discarding another card whose suit is different from that is not allowed.
        if cm.get_suit(leading_card) != cm.get_suit(card):
            if cm.is_suit_in_hand(self.hand, leading_card):
                return 0
            else:
                print('b')
                return 1

        # If the heart break has not been occured and the agent has a card with a suit other than heart,
        # discarding a heart card as a leading card is not allowed.
        #if not self.hb_flag and cm.is_not_heart_in_hand(self.hand) and cm.get_suit(card) == st.HEART:
        #    return 0

        return 1
