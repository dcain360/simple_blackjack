import Card

class Player:
	def __init__(self):
		self.money = 1000
		self.bet = 0
		self.hand = []
		self.isBlackjack = False
		self.hand_value = 0
		self.cardX = 0
	
		
	def add_card(self, card):
		try:
			self.hand.append(card)
			self.hand_value += card.get_value()
			
			if len(self.hand) == 2: 
				if self.hand_value == 21:
					if self.hand[0].name == "A" and self.hand[1].name in ["10", "J", "Q", "K"]:
						self.isBlackjack = True				
		except:
			print("could not compute player hand value")	
	
	def reset(self):
		self.hand = []
		self.hand_value = 0
		self.cardX = 0
		self.isBlackjack = False