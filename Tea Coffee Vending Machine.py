import sys
def cchoice():
	print('===================WELCOME TO TEA COFFEE VENDING MACHIENE===========================')
	print('1. TEA				10/-')
	print('2. COFFEE			10/-')
	print('3. BLACK TEA			10/-')
	print('4. BLACK COFFEE			10/-')
	print('5. ADMIN ENTRY')
	print('0. EXIT')
	print('\n\n')
	cc=int(input('ENTER YOUR CHOICE : '))
	if cc==1:
		otea()
	elif cc==2:
		ocoffee()
	elif cc==3:
		obtea()
	elif cc==4:
		obcoffee()
	elif cc==5:
		cadmin()
	elif cc==0:
		quit()
	else:
		invalid()
		cchoice()


def cadmin():
	print('================================WELCOME ADMIN====================================')
	print('1. CHECK CONTAINER STATUS')
	print('2. REFILL CONTAINERS')
	print('3. RESET SYSTEM')
	print('4. REPORTS')
	print("5. EXIT TO CUSTOMER's PAGE")
	print('0. EXIT MACHIENE')
	print('\n\n')
	ca=int(input('ENTER YOUR CHOICE : '))
	if ca==1:
		occstatus()
	elif ca==2:
		orcontainer()
	elif ca==3:
		ormachiene()
	elif ca==4:
		reports()
	elif ca==5:
		cchoice()
	elif ca==0:
		quit()
	else:
		invalid()
		cadmin()


def reports():
	print('======================================REPORTS============================================')
	print('1. DRINK WISE SALES')
	print('2. TOTAL SALE')
	print('0. ADMIN MENU')
	print('\n\n')
	cr=int(input('ENTER YOUR CHOICE : '))
	
	if cr==1:
		drink_wise_sale()
		reports()
	elif cr==2:
		print("Not made")
		reports()
	elif cr==0:
		cadmin()
	else:
		invalid()


tea=2000
coffee=2000
sugar=8000
water=15000
milk=10000
qtea=0
qbtea=0
qcoffee=0
qbcoffee=0

	

def otea():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea
	global qtea 
	qtea= int(input('Enter quantity : '))
	q = qtea
	while q>0:
		tea = tea - 15
		water = water - 60
		milk = milk - 40
		sugar = sugar - 15
		q=q-1
	print('DRINK SERVED.....GOOD DAY......VISIT AGAIN :)')
	cchoice()

def ocoffee():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea
	global qcoffee 
	qcoffee= int(input('Enter quantity : '))
	q = qcoffee
	while q>0:
		coffee = coffee - 4
		water = water - 20
		milk = milk - 80
		sugar = sugar - 15
		q=q-1
	print('DRINK SERVED.....GOOD DAY......VISIT AGAIN :)')
	cchoice()

def obtea():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea
	global qbtea
	qbtea= int(input('Enter quantity : '))
	q= qbtea
	while q>0:
		tea = tea - 3
		water = water - 100
		sugar = sugar - 15
		q=q-1
	print('DRINK SERVED.....GOOD DAY......VISIT AGAIN :)')
	cchoice()

def obcoffee():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea 
	global qbcoffee
	qbcoffee= int(input('Enter quantity : '))
	q=qbcoffee
	while q>0:
		coffee = coffee - 3
		water = water - 100
		sugar = sugar - 15
		q=q-1
	print('DRINK SERVED.....GOOD DAY......VISIT AGAIN :')
	cchoice()

def occstatus():
	print("Tea = ",tea)
	print("Coffee = ",coffee)
	print("Water = ",water)
	print("Sugar = ",sugar)
	print("Milk = ",milk)
	cadmin()

def orcontainer():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea
	tea = 2000
	coffee = 2000
	sugar = 8000
	water = 15000
	milk = 10000
	print('CONTAINERS RE-FILLED')
	cadmin()

def ormachiene():
	global milk
	global water 
	global sugar 
	global coffee 
	global tea
	tea = 0
	coffee = 0
	sugar = 0
	water = 0
	milk = 0
	print('SYSTEM RE-SET')
	cadmin()

def drink_wise_sale():
	print("Teas Sold : ",qtea)
	print("Coffees Slod : ",qcoffee)
	print("BLACK Teas Sold : ",qbtea)
	print("BLACK Coffees Sold : ",qbcoffee)

def invalid():
	print('INVALID INPUT TRY AGAIN')


def quit():
	sys.exit(0)



c=cchoice()
print(c)
