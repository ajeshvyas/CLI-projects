# -------------------------------------Class based progg-----------------------------------------------------

class Employee:

	def __init__(self):
		self.numEmployees = int(input("\nEnter no of employees to process : ")) # Number of empp to process
		self.empSalary = list()    # List of salries of emp
		self.benefits = list()     # List of benifits of emp respectively
		self.totalOperatingCost = 0    # Total operating cost of company initially 0

	def CalcOperating(self):
		for i in range(self.numEmployees):
			self.empSalary.append(float(input(f'\nEnter salary of Employee{i+1} : ')))     # Asking for salary
			s = input(f'\nIs employee{i+1} receiving (F)ull or (P)artial benefits? Please enter F or P : ')   # Asking for benefits
			self.benefits.append(s.lower())     # Adding benefit entered to the list
		# For calculating cost acc to respective benefit of emp
		for i in range(len(self.empSalary)):
			# If emp has full benefits - cost will be added by multiplication of salary with 1.5
			if self.benefits[i] == 'f':
				self.totalOperatingCost += self.empSalary[i]*1.5
			# If emp has partial benefits - cost will be added by multiplication of salary with 1.25
			else:
				self.totalOperatingCost += self.empSalary[i]*1.25
		# Finally printing Result with 2 decimal places of cost.
		print(f'\nYour total operating cost is : {self.totalOperatingCost:.2f}')


w = True                                # For repeatation of loop
while w:								# Loop for menu representation of never ending progg untill user decides
	
	# Welcome message
	print('\n\n',"*"*35,'Welcome to Company Cost of Operation Evaluator','*'*35,'\n')
	# Asking user to start calculation or to exit
	c = int(input('\n-1-Start calculation\n-0-Exit\nPlease select any option : '))
	# If user selects to exit the progg - Exit with thankyou message
	if c == 0:
		print("\nThankyou, visit again!!!\n\n")
		w = False
	# If user selects wrong option - Says to enter correct option
	elif c != 0 and c != 1:
		print('\nWrong selection, Please try again...')
	# If user selects to calculate then calculation below
	else:
		emp = Employee()				# Creating class object
		emp.CalcOperating()				# Calling class method