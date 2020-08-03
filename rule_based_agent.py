import math
import agent
import common as cm
import settings as st

class Rule_based_agent(agent.Agent):

    def select_card(self, card_history, agent_history, trick, turn):

        # If the agent has C-2, it has to discard the card.
        if not trick and not turn:
            idx = cm.is_card_in_hand(self.hand, st.C_2)
            if idx:
                self.hand[idx] = -1
                return st.C_2
            else:
                print('ValueError: rule_based_agent.py in line 17')
                sys.exit(self.hand)

        score = [-10000] * st.NUM_KC
        for i, card in enumerate(self.hand):
            if card == -1:
                continue
            elif not self.validate_card(card, card_history[trick], trick, turn):
                continue
            else:
                score[i] = self.scoring_card(card_history, agent_history, trick, turn, card)

        max = -10000
        max_index = -1
        card = -1
        for i in range(st.NUM_KC):
            if self.hand[i] == -1:
                continue
            else:
                if score[i] > max:
                    max = score[i]
                    max_index = i
                    card = self.hand[i]
        self.hand[max_index] = -1
        return card

    def scoring_card(self, card_history, agent_history, trick, turn, card):

        # When the first turn,
        if not turn:
            return 2
        # When the following terns,
        else:
            leading_card = card_history[trick][0]
            if card == st.S_Q:
                # If the suit of the leading card is not SPADE, the agent must immediately discard S-Q.
                if cm.get_suit(leading_card) != st.SPADE:
                    return 10000
                # Even if the suit of the leading card is SPADE,
                # when a former card that is stronger than S-Q has already discarded, the agent must immediately discard S-Q.
                else:
                    if cm.is_stronger_card_discarded(card_history[trick], card):
                        return 5000
                    else:
                        return -1000

            if card >= st.H_2:
                if cm.get_suit(leading_card) != st.HEART:
                    return math.exp(card/10)
                else:
                    return 3

            return 1
