import random
import time
#import numpy as np

##requirement: Ask user how many playing card decks to play with?
while True:
  try:
    x = int(input("How many playing card decks (maximum 1 only): "))
    if x == 1:
      break
    elif x > 1:
      print("Maximum 1 deck sorry") 
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
    for c in self.cards:
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
    ## list attribute hand
    self.hand = []
    
  #def __repr__(self):
    ##

  ## player draws from deck
  def draw(self, deck):
    self.hand.append(deck.drawCard())
    return self

  ## player shows hand
  def showHand(self):
    for card in self.hand:
      card.show()

  ## player removes card from hand
  def playCard(self):
     return self.hand.pop()
     
  ## need to find way to append winning cards from snap game
  def takeCards(self, winnings):
     self.hand.append(winnings)
     return self


## Create deck object
deck = Deck()

## Shuffle deck
deck.shuffle()

## Simulate game 
# create player instances
p1 = Player()
p2 = Player()

## Draw from deck/Deal cards, player gets 26 cards each 
for i in range(1, 27):
  p1.draw(deck)
  p2.draw(deck)

count = 1
## players yell snap at random
a = ["Player 1:", "Player 2:"]
## list represents non-match played hands
tmp = []
while count <= 26:
    x = p1.playCard()
    y = p2.playCard()
    ## using value match so there's more liklihood of a snap.
    if x.value == y.value:
        print("-----------------------------------------------------------")
        print("Player 1:") 
        x.show()
        print("Player 2:")
        y.show()

        ## select random winner
        winner = random.choice(a)
        print("\n", winner)
        print(" \"Snap!!!!!\"\n")
        if winner == "Player 1:":
          #print(winner)
          print("The winner of this round is: {}".format(winner))
          p1.takeCards(x)
          p1.takeCards(y)
          for t in tmp:
            p1.takeCards(t)
        elif winner == "Player 2:":
          #print(winner)
          print("Winner is: {}".format(winner))
          p2.takeCards(x)
          p2.takeCards(y)
          for t in tmp:
            p2.takeCards(t)
        count+=1
        time.sleep(1)
        break
    else: 
        print("-----------------------------------------------------------")
        print("Player 1:") 
        x.show()
        tmp.append(x)
        print("Player 2:") 
        y.show()
        tmp.append(y)
        print("No match!\n")
        count+=1
        time.sleep(1)
        #sys.stdout.flush()

print("\n//////////PLAYER 1 HAND:")
p1.showHand()
print("-------------------------------------------------------------------\n")
print("////////////PLAYER 2 HAND:")
p2.showHand()
print("-------------------------------------------------------------------\n")