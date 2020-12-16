import random as r  # For generating random values
class BlackJack:

	def __init__(self,A):
		self.A=A  
		self.v=[1,2,3,4,5,6,7,8,9,10,'A','K','Q','J']   #List to generate random values from
		self.d1=r.choice(self.v)                        #Value of dealer's card 1
		self.d2=r.choice(self.v)						#value of dealer's card 2
		self.d3=0										#value of dealer's card 3 in case to be used
		self.p1=r.choice(self.v)						#Value of Player's card 1
		self.p2=r.choice(self.v)						#Value of Player's card 2
		self.p3=0										#value of Player's card 3 in case to be used

	def main(self):
# ----------------------------------print card values of dealer and player----------------------------
		print(f"\nDealer has x and {self.d2}")            # one value of dealer's card should be hidden as 'x'
		print(f"Player has {self.p1} and {self.p2}\n")
		print("_"*74)
# ------------------------------------Asking player for to choose from stand or to hit---------------
		print("\n-1-Hit (Ask for another card)\n-2-Stand (Continue to declare)\n")
		c=int(input("Enter your choice : "))
		print("_"*74,'\n')
# -----------------------------conditions if player decides to hit---------------------------
		if c==1:
			self.d3=r.choice(self.v)
			self.p3=r.choice(self.v)
			print("_"*74,'\n')
			print(f"\nDealer has x, {self.d2}, {self.d3}")
			print(f"Player has {self.p1}, {self.p2}, {self.p3}\n")
			print("_"*74)
# -------------------------------Conditions if value of card is not a number-----------------------
# ---------------Here if value of card is K,A,Q and J then value will be 10------------------------
# --------------And the value id A then User decided value will be assigned-----------------------
# ------------------Here as a rule of game player and dealer both will get a card----------------
			if self.d1=="A" or self.d1=="Q" or self.d1=="J" or self.d1=="K":
				if self.d1=="A":
					self.d1=self.A
				else:
					self.d1=10
			else:
				pass
			if self.d2=="A" or self.d2=="Q" or self.d2=="J" or self.d2=="K":
				if self.d2=="A":
					self.d2=self.A
				else:
					self.d2=10
			else:
				pass
			if self.d3=="A" or self.d3=="Q" or self.d3=="J" or self.d3=="K":
				if self.d3=="A":
					self.d3=self.A
				else:
					self.d3=10
			else:
				pass
			if self.p1=="A" or self.p1=="Q" or self.p1=="J" or self.p1=="K":
				if self.p1=="A":
					self.p1=self.A
				else:
					self.p1=10
			else:
				pass
			if self.p2=="A" or self.p2=="Q" or self.p2=="J" or self.p2=="K":
				if self.p2=="A":
					self.p2=self.A
				else:
					self.p2=10
			else:
				pass
			if self.p3=="A" or self.p3=="Q" or self.p3=="J" or self.p3=="K":
				if self.p3=="A":
					self.p3=self.A
				else:
					self.p3=10
			else:
				pass
# ----------------------Getting sum of values of Dealer's and player's Card------------------
			s_p=self.p1+self.p2+self.p3
			s_d=self.d1+self.d2+self.d3
# ----------------------Getting results according to conditions of game----------------------
			if s_p>21:
				print("Dealer is winner as Player has value more than 21")
			elif s_p>s_d:
				print(f"Player is winner as Player value is {s_p} and dealer value is {s_d}")
			elif s_p<s_d:
				print(f"Dealer is winner as Player value is {s_p} and dealer value is {s_d}")
			else:
				print("You both have same value")
			print(f"Dealer's value : {s_d}")
			print(f"Player's value : {s_p}")
			print("_"*74,'\n')
# -----------------------------conditions if player decides to stand---------------------------
		else:
			if self.d1=="A" or self.d1=="Q" or self.d1=="J" or self.d1=="K":
				if self.d1=="A":
					self.d1=self.A
				else:
					self.d1=10
			else:
				pass
			if self.d2=="A" or self.d2=="Q" or self.d2=="J" or self.d2=="K":
				if self.d2=="A":
					self.d2=self.A
				else:
					self.d2=10
			else:
				pass
			if self.p1=="A" or self.p1=="Q" or self.p1=="J" or self.p1=="K":
				if self.p1=="A":
					self.p1=self.A
				else:
					self.p1=10
			else:
				pass
			if self.p2=="A" or self.p2=="Q" or self.p2=="J" or self.p2=="K":
				if self.p2=="A":
					self.p2=self.A
				else:
					self.p2=10
			else:
				pass
# ----------------------Getting sum of values of Dealer's and player's Card------------------
			s_p=self.p1+self.p2
			s_d=self.d1+self.d2
# ----------------------Getting results according to conditions of game----------------------
			if s_p>21:
				print("Dealer is winner as Player has value more than 21")
			elif s_p>s_d:
				print(f"Player is winner as Player value is {s_p} and dealer value is {s_d}")
			elif s_p<s_d:
				print(f"Dealer is winner as Player value is {s_p} and dealer value is {s_d}")
			else:
				print("You both have same value")
			print(f"Dealer's value : {s_d}")
			print(f"Player's value : {s_p}")
			print("_"*74,'\n')




# Loop for menu and repeatation of progg.
w=True

while w==True:
	print("-"*74)
	# print("\n")
	print("_"*25,"Welcome to BlackJack21","_"*25,"\n")
	c=int(input("-1-Play\n-2-Exit\nEnter your choice : "))
	if c==1:
		a=0
		c=int(input("\n-1-Value 1\n-2-Value 11\nEnter value of Ace to be used in game : "))  # Input for value of Ace
		if c==1:
			a=1
			bj=BlackJack(a)
			bj.main()
		elif c==2:
			a=11
			bj=BlackJack(a)
			bj.main()
		else:
			print("Wrong value try again")
	elif c==2:
		w=False
		print("\nThankyou for playing BlackJack21\n")
	else:
		print("Wrong choice, try again")