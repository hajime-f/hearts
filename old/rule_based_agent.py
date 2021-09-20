#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import agent
import common as cm
import settings as st

class Rule_based_agent(agent.Agent):

    INF = 10000

    def select_card(self, card_history, agent_history, trick, turn):

        # If the agent has C-2, it has to discard the card.
        if not trick and not turn:
            idx = cm.is_card_in_hand(self.hand, st.C_2)
            if idx >= 0:
                self.hand[idx] = -1
                return st.C_2
            else:
                print('ValueError: rule_based_agent.py in line 17')
                sys.exit(self.hand)

        score = [-self.INF] * len(self.hand)
        for i, card in enumerate(self.hand):
            if card == -1:
                continue
            elif not self.validate_card(card, card_history[trick], trick, turn):
                continue
            else:
                score[i] = self.scoring_card(card_history, agent_history, trick, turn, card)

        # The agent discards the card whose score is max.
        max_index = score.index(max(score))
        card = self.hand[max_index]
        self.hand[max_index] = -1
        return card

    def scoring_card(self, card_history, agent_history, trick, turn, card):
        if not turn:
            return self.scoring_card_first_turn(card_history, agent_history, trick, card)
        else:
            return self.scoring_card_following_turn(card_history, agent_history, trick, turn, card)

    def scoring_card_first_turn(self, card_history, agent_history, trick, card):

        turn = 0
        suit = cm.get_suit(card)

        if card == st.S_K or card == st.S_A:
            if not cm.is_card_discarded_in_game(card_history, st.S_Q):
                return -self.INF + 1

        if card == st.S_Q:
            c_list = cm.get_remaining_card_list(card_history, self.hand, suit)
            if c_list[0:st.NUM_KC-3].count(1) + c_list[0:st.NUM_KC-3].count(2) >= st.NUM_KC - 5:
                #print(c_list, c_list[0:st.NUM_KC-3].count(1) + c_list[0:st.NUM_KC-3].count(2))
                #sys.exit()
                return self.INF
            else:
                return -self.INF + 1

        return 2

    def scoring_card_following_turn(self, card_history, agent_history, trick, turn, card):

        leading_card = card_history[trick][0]
        suit = cm.get_suit(card)

        if card == st.S_Q:
            # If the suit of the leading card is not SPADE, the agent must immediately discard S-Q.
            if cm.get_suit(leading_card) != st.SPADE:
                return self.INF
            else:
                # Even if the suit of the leading card is SPADE,
                # when a former card that is stronger than S-Q has already discarded, the agent must immediately discard S-Q.
                if cm.is_stronger_card_discarded(card_history[trick], card):
                    return self.INF
                else:
                    return -self.INF + 1

        if suit != cm.get_suit(leading_card):
            if card == st.S_A:
                return self.INF - 1
            elif card == st.S_K:
                return self.INF - 2
            elif suit == st.HEART:
                heart_num = st.NUM_KC - cm.get_discarded_suit_number(card_history, st.HEART)
                stronger_heart_num = cm.get_remaining_stronger_card_number(card_history, card)
                return self.validate_score(8000 - (stronger_heart_num / heart_num) * 8000 + math.exp(card/10))

        if suit == st.HEART:
            if cm.is_stronger_card_discarded(card_history[trick], card):
                return self.validate_score(math.exp(card/6))
            else:
                return self.validate_score(-math.exp(card/6))

#        if suit != cm.get_suit(leading_card):

        if turn == st.NUM_PR-1 and cm.get_suit(leading_card) != st.HEART:
            if card == st.S_K:
                return -self.INF + 1
            if card == st.S_A:
                return -self.INF + 2

        if suit == st.SPADE and suit == cm.get_suit(leading_card):
            if card == st.S_K and cm.is_card_discarded(card_history[trick], st.S_A):
                return self.INF - 1
            if (card == st.S_K or card == st.S_A) and cm.is_card_discarded(card_history[trick], st.S_Q):
                return -self.INF + 1
            if not cm.is_card_discarded_in_game(card_history, st.S_Q):
                if card == st.S_K:
                    return -self.INF + 2
                if card == st.S_A:
                    return -self.INF + 1
            if turn == st.NUM_PR - 1 and not cm.is_card_discarded(card_history[trick], st.S_Q) and trick <= st.NUM_KC / 2:
                if card == st.S_K:
                    return self.INF - 2
                if card == st.S_A:
                    return self.INF - 1                

        return 1

    def validate_score(self, score):
        if score > self.INF:
            return self.INF - 1
        if score < -self.INF:
            return -self.INF + 1
        return score
