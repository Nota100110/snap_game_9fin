import random
import time
#import numpy as np

## 1) Requirement: Ask user how many playing card decks to play with?
while True:
	try:
		x = int(input("How many playing card decks: "))
		if x == 2:
			break
		elif x > 2:
			print("Maximum 2 players sorry") 
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")


## Create class Card, create instances of objects by assigning to suit and value
## These are set to whatever we pass in when creating a card
class Card(object):
	"""docstring for Card"""
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	## another method to show cards, takes self - will print out value and suit
	def show(self):
		print("{} of {}".format(self.value, self.suit))

## Create class Deck
class Deck(object):
	def __init__(self):
		## initialise an attribute called cards
		self.cards = []
		#method to build deck, takes self, creating 52 cards
		self.build()

	## method build() declaration, creating suits/cards 
	## 1-14 non-inclusive
	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			#non-inclusive
			for v in range(1, 14):
				#print(v)
				#print("{} of {}".format(v, s))
				self.cards.append(Card(s, v))

	def show(self):
		for	c in self.cards:
			c.show()

	## shuffle method (fisher gates)
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			#print(i)
			r = random.randint(0, i)
			## swap two cards
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	## draw card method
	## removes and returns the last value from the List or the given index value
	def drawCard(self):
		return self.cards.pop()

class Player(object):
	def __init__(self):
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for card in self.hand:
			card.show()

	def discard(self):
		return self.hand.pop()


## create deck object 
deck = Deck()

## 2) Requirement: application should shuffle deck
## shuffle deck
deck.shuffle()

## rebuild deck
#deck.build()


## 3) Requirement: Simulate game 

print("CARD GAME COMMENCING!!!\n")

## Player 1
p1 = Player()
#p2.draw(deck).draw(deck)
p1.draw(deck)
p1.showHand()

## Player 2
p2 = Player()
#p2.draw(deck).draw(deck)
p2.draw(deck)
p2.showHand()

