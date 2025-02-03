import Card

class Player:
	def __init__(self):
		self.money = 1000
		self.hand = []
		self.hand_value = 0
		self.cardX = 0
	
	def add_card(self, card):
		try:
			self.hand.append(card)
			self.hand_value += card.get_value()
		except:
			print("could not compute player hand value")	
		
	def reset(self):
		self.hand = []
		self.hand_value = 0
		self.cardX = 0