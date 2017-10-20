from deck_cards import Deck
from player import Player

class Game(object):
  
  def __init__(self,deck):
    self.players = []
    self.rounds = 0

    while(True):
      number_players = int(input("How many players? "))

      if(number_players > 4 or number_players < 1):
        print("Please enter a number between 1 and 4")
      else:
        break

    for i in range(number_players):
      name = raw_input("Enter player {}'s name: ".format(i+1))
    
      self.players.append(Player(name, deck))
    
    print "------------------------"
    print "DEALING CARDS TO PLAYERS"
    print "------------------------"
    print
    for i in range(52/len(self.players)):
      for player in self.players:
        player.deal(1, deck)
    
    
    print "------------------------"
    print "CARDS HAVE BEEN DEALT"
    print "------------------------"
    print

    print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for player in self.players:
      print "				| {} has {} cards! ".format(player.name, len(player.hand))
    print"                                |  >round: {}".format(self.rounds)
    print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    adv = raw_input('>>>>Press enter to play or type exit to quit!')
    print 
    
    self.main_loop()


  def play_round(self):
    active_cards = []
    war = False
    self.rounds += 1

    for player in self.players:
      active_cards.append(player.hand[0])
      print "		-------->	{} plays a {} of {}".format(player.name, player.hand[0][0], player.hand[0][1])
      player.remove_card(player.hand[0])

    card_values = [0]*len(active_cards)
    for i in range(len(active_cards)):
      card_values[i] = self.get_value(active_cards[i][0])
 
    best_card = max(card_values)
    best_index = card_values.index(best_card)


    for i in range(len(active_cards)):
      if(i != best_index):
        if(card_values[i] == best_card):
          print "	####################"
          print "	#XXXX   WAR!   XXXX#"
          print "	####################" 
          adv = raw_input("------> Press enter to continue!")
          self.war_scenario(active_cards, best_index, i)
          war = True


    if(not war):
      print
      print "========>{} wins the round!".format(self.players[best_index].name)
      print
      
      for i in range(len(self.players)):
        if(i == best_index):
          self.players[i].add_cards(active_cards) 

      print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      for player in self.players:
        print "				|  {} has {} cards! ".format(player.name, len(player.hand))
      print"                                |  >round: {}".format(self.rounds)
      print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


  # This function handles all the logic for the situations in which two players put down a card with
  # the exact same value. First, add both the active cards to the limbo pile. Then, for each player,
  # if they have more than three cards in their hand, gather three more for the limbo pile, otherwise 
  # grab as many as we can and still leave one card in their hand.
  def war_scenario(self, active_cards, player1_ind, player2_ind):
    print "	    []     []"
    print "	    []     []"
    print "	    []     []"

    cards_in_limbo = active_cards
    war = False
    self.rounds += 1

    if(len(self.players[player1_ind].hand) > 3):
      for i in range(3):
        cards_in_limbo.append(self.players[player1_ind].hand[0])
        self.players[player1_ind].remove_card(self.players[player1_ind].hand[0])

    else:
      for i in range(len(self.players[player1_ind].hand)-1):
        cards_in_limbo.append(self.players[player1_ind].hand[0])
        self.players[player1_ind].remove_card(self.players[player1_ind].hand[0])

    if(len(self.players[player2_ind].hand) > 3):
      for i in range(3):
        cards_in_limbo.append(self.players[player2_ind].hand[0])
        self.players[player2_ind].remove_card(self.players[player2_ind].hand[0])

    else:
      for i in range(len(self.players[player2_ind].hand)-1):
        cards_in_limbo.append(self.players[player2_ind].hand[0])
        self.players[player2_ind].remove_card(self.players[player2_ind].hand[0])

          
    new_active_cards = []

    new_active_cards.append(self.players[player1_ind].hand[0])
    print "		-------->	{} plays a {} of {}".format(self.players[player1_ind].name, self.players[player1_ind].hand[0][0], self.players[player1_ind].hand[0][1])
    self.players[player1_ind].remove_card(self.players[player1_ind].hand[0])


    new_active_cards.append(self.players[player2_ind].hand[0])
    print "		-------->	{} plays a {} of {}".format(self.players[player2_ind].name, self.players[player2_ind].hand[0][0], self.players[player2_ind].hand[0][1])
    self.players[player2_ind].remove_card(self.players[player2_ind].hand[0])



    card_values = [0]*len(new_active_cards)
    for i in range(len(new_active_cards)):
      card_values[i] = self.get_value(new_active_cards[i][0])

    best_card = max(card_values)
    best_index = card_values.index(best_card)

    for i in range(len(new_active_cards)):
      if(i != best_index):
        if(card_values[i] == best_card):
          print "	  ####################"
          print "    	  #XXXX   WAR!   XXXX#"
          print "	  ####################" 
          adv = raw_input( "------> Press enter to continue!")
          self.war_scenario(new_active_cards+cards_in_limbo, best_index, i)
          war = True


    if(not war):
      print
      print "========>{} wins the round!".format(self.players[best_index].name)
      print
      
      self.players[best_index].add_cards(new_active_cards + cards_in_limbo) 

          
      print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      for player in self.players:
        print "				| {} has {} cards! ".format(player.name, len(player.hand))
      print"                                |  >round: {}".format(self.rounds)
      print"				~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


  def main_loop(self):

    game = True
    manual_exit = False
  
    while(game):

      if(self.rounds != 0):
        print"...................................................."
        adv = raw_input(">>>>Press enter to play another round or type exit to quit!")
        print"...................................................."
        print

        if(adv.lower() == "exit"):
          game = False
          manual_exit = True

      self.play_round()
  
      for player in self.players:
        if(player.hand == []):
          print '///////{} HAS BEEN REMOVED FROM THE GAME'.format(player.name)
          self.players.remove(player)

      if(len(self.players) == 1):
        game = False

    if(not manual_exit):
      print"#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#"
      print"#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#"
      print"         >>>>>>>>>>>>> {} IS THE WINNER! <<<<<<<<<<<<<<<<<".format(self.players[0].name)
      print"#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#"
      print"#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#"

    else:
      print">>>>>>>>>>>>>>>>>>Game has been stopped"


  def get_value(self, card):
    try:
      value = int(card)

    except ValueError:
      if(card == 'Jack'):
        value = 11
      elif(card == 'Queen'):
        value = 12
      elif(card == 'King'):
        value = 13
      elif(card == 'Ace'):
        value = 14

    return value
     

deck = Deck()

new_game = Game(deck)
