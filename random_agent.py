import agent
import settings as st

class Random_agent(agent.Agent):

    def select_card(self, card_history, agent_history, trick, turn):
        for h in range(st.NUM_KC):
            if self.hand[h] == -1:
                continue
            elif not self.validate_card(self.hand[h], card_history[trick], trick, turn):
                continue
            else:
                card = self.hand[h]
                self.hand[h] = -1
                return card
        return -1
