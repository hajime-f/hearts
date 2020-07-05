import agent
import settings as st

class Random_agent(agent.Agent):

    def select_card(self, card_history, agent_history, trick, turn):
        for i in range(st.NUM_KC):
            if self.hand[i] == -1:
                continue
            elif not self.validate_card(self.hand[i], card_history[trick], trick, turn):
                continue
            else:
                card = self.hand[i]
                self.hand[i] = -1
                return card
        return -1
