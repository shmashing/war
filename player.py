from deck_cards import Deck

class Player(object):
  
  def __init__(self, name, deck):
    self.name = name
    self.hand = []

  def deal(self, numb_cards, deck):
    for i in range(numb_cards):
      self.hand.append(deck.draw_card())

  def print_hand(self):
    print "{}'s hand:".format(self.name)
    for i in range(len(self.hand)):
      print "{} of {}".format(self.hand[i][0], self.hand[i][1])

    print

  def remove_card(self, card):
    self.hand.remove(card)

  def add_cards(self, cards):
    for card in cards:
      self.hand.append(card)

 

