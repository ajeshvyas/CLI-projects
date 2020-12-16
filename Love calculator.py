class Love_Calculator:                # calculator class

	def __init__(self,u,p):           # Constructor with user name and partner's name
		self.user = u
		self.partner = p

	def calculator(self):             # Calculator method which calculates the result
		user_sum = 0                      #Sum of alphabets of user's name
		partner_sum = 0					  # sum of alphabets of partner's name
		# To convert alphabets of respective names into ASCII and store their addition in respective variables as above
		for i in self.user:                    
			user_sum += ord(i)-96
		for i in self.partner:
			partner_sum += ord(i)-96

		us = 0							# Sum of each digit of user_sum
		ps = 0							# sum of each digit of oartner_sum
		# To store sum of each digits of the sum obtain by addition of ascii of alphabets into respective variables as above
		for i in str(user_sum):
			us += int(i)

		for i in str(partner_sum):
			ps += int(i)
		# Result wirh sum of us, ps and 'LOVE' letter's ascii sum
		r = us+ps+54

		print(f"\n\nLove Percentage between {self.user} and {self.partner} is {r}%\n")   # Printing the result acordingly

		print("-"*50,'\n\n')

w = True				# To put menu in loop untill exit by user
while w:
	print("-------------------------------------Welcome to Love Calculator-----------------------------------\n\n")

	# Menu asking user to calculate or to exit the progg.
	c = int(input("-1-Calculate Love\n-0-Exit\nPlease select a valid option : "))
	# Conditions according to selection of user
	if c==0:                     # If selects to exit
		w=False
		print("\nThankyou, Visit again please.\n\n")
	elif c!=0 and c!=1:          # If user puts a wrong option
		print("\nWrong selection, Please select a valid option\n\n")
	else:							# If user selects to calculate
		print('\n')
		print("-"*50)
		# Asking user to enter perticular names while instantiating class object
		c = Love_Calculator(input("\n\nEnter your name : ").lower(),input("Enter partner's name : ").lower())
		print('\n')
		print("-"*50)
		c.calculator()