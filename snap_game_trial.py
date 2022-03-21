"""

SNAP !!

"""

import itertools
import random
import time

## How to generate numbers faster 

## Asks users how many playing card decks required
decks = input("How many playing card decks to play with?  ")
print("\n\nNumber of decks: " + decks)
print("\n")

## Create the decks of cards use .product function
## dict elements 0[] 1[]
deck1 = list(itertools.product(["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],["Spade", "Club", "Diamond", "Heart"]))
deck2 = list(itertools.product(["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],["Spade", "Club", "Diamond", "Heart"]))

## Shuffle the decks of cards
random.shuffle(deck1)
random.shuffle(deck2)

## print decks
Deck1 = []
Deck1.append(deck1)
#print(Deck1)

Deck2 = []
Deck2.append(deck2)
#print(Deck2)

print("CARD GAME COMMENCING!!!\n")
for i in range (1, 52):
	## below for exact cards
	#if deck1[i][0] + deck1[i][1] == deck2[i][0] + deck2[i][1]:
	#below won't check for suits
	if deck1[i][0] == deck2[i][0]:
		print("SNAP!")
		print(deck1[i][0] + deck1[i][1], deck2[i][0] + deck2[i][1])
		print("...\n")
		time.sleep(3) # Sleep for 3 seconds
		pass