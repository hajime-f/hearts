from abc

class Agent(metaclass = abc.ABCMeta):

    hand = []
    hb_flag = 0

    def __init__(self):
        pass

    def set_cards(self, cards):
        self.hand = cards.copy()
        hb_flag = 0

    @abc.abstractmethod
    def select_card(self, card_history, agent_history):
        pass

    def validate_card(self, card, card_history, trick, turn ):

        # In the first turn of the first trick C-2 must be discarded.

        # In the first trick, discarding S-Q is not allowed.

        # In the first trick, discarding heart cards is not allowed.

        # 
