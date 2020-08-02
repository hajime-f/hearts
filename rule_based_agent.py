import math
import agent
import common as cm
import settings as st

class Rule_based_agent(agent.Agent):

    def select_card(self, card_history, agent_history, trick, turn):
        score = [-10000] * st.NUM_KC
        for i in range(st.NUM_KC):
            if self.hand[i] == -1:
                continue
            elif not self.validate_card(self.hand[i], card_history[trick], trick, turn):
                print('c')
                continue
            else:
                card = self.hand[i]
                # When the first turn,
                if not turn:
                    continue
                # When the following terns,
                else:
                    leading_card = card_history[trick][0]
                    if card == st.S_Q:
                        # If the suit of the leading card is not SPADE, the agent must immediately discard S_Q.
                        if cm.get_suit(leading_card) != st.SPADE:
                            del score
                            self.hand[i] = -1
                            return card
                        # Even if the suit of the leading card is SPADE,
                        # when a former card that is stronger than the card has already discarded, the agent must immediately discard S_Q.
                        else:
                            if cm.is_stronger_card_discarded(card_history[trick], card):
                                del score
                                self.hand[i] = -1
                                return card
                            else:
                                score[i] = -100
                    if card >= st.H_2:
                        if cm.get_suit(leading_card) != st.HEART:
                            score[i] = math.exp(card/10)
        max = -10000
        card = -1
        print(score)
        for i in range(st.NUM_KC):
            if self.hand[i] == -1:
                continue
            else:
                if score[i] > max:
                    print('a')
                    max = score[i]
                    card = self.hand[i]
                    print(card)
        del score
        self.hand[i] = -1
        return card
