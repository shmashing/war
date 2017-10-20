from random import *
#
#  DECK CLASS
######################################
class Deck(object):

  def __init__(self):
    self.cards = {'clubs': [],'hearts': [],'diamonds': [],'spades': []}
    self.build()

  def build(self):
    suits = ['clubs', 'hearts', 'diamonds', 'spades']

    cards = []
    for i in range(len(suits)):
      for j in range(2, 15):
        if(j <= 10):
          self.cards[suits[i]].append(str(j))
        elif(j == 11):
          self.cards[suits[i]].append('Jack')
        elif(j == 12):
          self.cards[suits[i]].append('Queen')
        elif(j == 13):
          self.cards[suits[i]].append('King')
        elif(j == 14):
          self.cards[suits[i]].append('Ace')
 

  def print_cards(self):
    for suit in self.cards:
      for i in range(len(self.cards[suit])):
        print "{} of {}".format(self.cards[suit][i], suit)
  

  def draw_card(self):

    suit_to_delete = ''    
    for suit in self.cards:
      if(self.cards[suit] == []):
        suit_to_delete = suit

    if(suit_to_delete != ''):
      del self.cards[suit_to_delete]

    # Pick a random suit
    suit = choice(self.cards.keys())

    # Within the random suit, pick a random card
    if(len(self.cards[suit]) > 1):
      rand_card = randint(0, len(self.cards[suit])-1)

    elif(len(self.cards[suit]) == 1):
      rand_card = 0

    # Identify the exact card
    # And remove it from the deck of cards
    card = [self.cards[suit][rand_card], suit]
    self.cards[suit].pop(rand_card)

    # then return it
    return card


