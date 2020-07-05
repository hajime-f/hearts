# Number of suits: Spade, Heart, Diamond and Club
NUM_SUITS = 4

CLUB = 0
DIA = 1
SPADE = 2
HEART = 3

# Number of cards in each suit: 2-10, J, Q, K and A
NUM_KC = 13

# Number of all cards
NUM_CARDS = NUM_SUITS * NUM_KC

# Total number of games
NUM_GAMES = 100

# Number of players: Hearts is played by four players.
NUM_PR = 4

C_2 = 0
S_Q = SPADE * NUM_KC + 10
H_2 = HEART * NUM_KC

# File name for writing the result
FILE_NAME = 'result.log'

# for debug
CARD_NAME = ['C-2', 'C-3', 'C-4', 'C-5', 'C-6', 'C-7', 'C-8', 'C-9', 'C-10', 'C-J', 'C-Q', 'C-K', 'C-A',
             'D-2', 'D-3', 'D-4', 'D-5', 'D-6', 'D-7', 'D-8', 'D-9', 'D-10', 'D-J', 'D-Q', 'D-K', 'D-A',
             'S-2', 'S-3', 'S-4', 'S-5', 'S-6', 'S-7', 'S-8', 'S-9', 'S-10', 'S-J', 'S-Q', 'S-K', 'S-A',
             'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'H-7', 'H-8', 'H-9', 'H-10', 'H-J', 'H-Q', 'H-K', 'H-A' ]
