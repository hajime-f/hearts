import agent
import settings as st

class Random_agent(agent.Agent):

    def select_card(self, card_history, agent_history, trick, turn):
        for card in range(st.NUM_KC):
            if self.hand[card] == -1:
                continue
            elif not self.validate_card(self.hand[card], card_history[trick], trick, turn):
                continue
            else:



        return -1
