#Python 	- Blackjack
#Versão		- 1.0.0
#Author 	- Flavio

#Embaralhar cartas
import random

playing = False
chip_pool = 100
bet = 1

restart_phrase = "Press 'd' to play again or 'q' to leave"

suits = ('H', 'D', 'C', 'S')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K')

card_val = {'A' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10}

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	def __str__(self):
		return self.suit + self.rank
		
	def grab_suit(self):
		return self.suit
	
	def grab_rank(self):
		return self.rank
	
	def draw(self):
		print(self.suit + self.rank)
		
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = False
		
	def __str__(self):
		hand_comp = ""
		
		for card in self.cards:
			card_name = card.__str__()
			hand_comp += " " + card_name
			
		return "A mão tem {}".format(hand_comp)
		
	def card_add(self, card):
		self.cards.append(card)
		
		if card.rank == 'A'
			self.ace = True
			
		self.value += card_val[card.rank]
		
	def calc_val(self):
		if self.ace == 'True' and self.value < 12:
			return self.value + 10
		
		else:
			return self.value
			
	def draw(self, hidden):
		if hidden and playing:
			starting_card = 1
		else:
			starting_card = 0;
			
		for x in range(starting_card, len(self.cards)):
			self.cards[x].draw()
			
class Deck:
	def __init__(self):
		self.deck = []
		
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit, rank))
				
	def shuffle(self):
		random.shuffle(self.deck)
		
	def deal(self):
		single_card = self.deck.pop()
		return single_card
		
	def __str__(self):
		deck_comp = ""
		for card in self.deck:
			deck_comp += " " + card.__str__()
			
		return "O baralho tem " + deck_comp
		
def make_bet():
	global bet
	bet = 0
	
	print("Quanto você deseja apostar? (Apenas números inteiros)")
	
	while bet == 0:
		bet_comp = int(input())
		
		if bet_comp >= 1 and bet_comp <= chip_pool:
			bet = bet_comp
			
		else:
			print("Aposta inválida. Você tem {} ficas sobrando").format(chip_pool)
			
def deal_cards():
	global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
	deck = Deck()
	deck.shuffle()
	
	make_bet()
	
	player_hand = Hand()
	dealer_hand = Hand()
	
	player_hand.card_add(deck.deal())
	player_hand.card_add(deck.deal())
	
	dealer_hand.card_add(deck.deal())
	dealer_hand.card_add(deck.deal())
	
	result = "Bater ou parar? Pressione 'h' ou 's'"
	
	playing = True
	
	game_step()
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		