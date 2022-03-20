#import tkinter
import turtle 
import sys
import os

#os.system("Xvfb :1 -screen 0 720x720x16 &")
#os.environ['DISPLAY'] = ":2.0"

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Snap card game simulator")

class Card():
	def __init__(self, name, suit):
		self.name = name 
		self.suit = suit

	def print_card(self):
		print(self.name, self.suit)

card = Card("A", "S")
card.print_card()