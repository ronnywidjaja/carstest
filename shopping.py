your_cart = []
total = 0

def items():
	category = ['Dairy', 'Fruits', 'Vegetables', 'Meats', 'Sweets']
	list_product = [[['Milk',2],['Cheese',5],['Butter',1]],
				[['Apple',1],['Orange',1],['Banana',1]],
				[['Spinach',0.5],['Brocolli',1],['Cabbage',1]],
				[['Pork',2],['Beef',3],['Lamb',4]],
				[['Chocolate',2],['Candy',1],['Cookies',1]]]
				
	products = { 'milk':2,'cheese':5, 'butter':1 ,'apple':1,'orange':1,'banana':1,'spinach':0.5,'brocolli':1,'cabbage':1,'pork':2,'beef':3,'lamb':4,'chocolate':2,'candy':1,'cookies':1	}
				
	for index in range(len(category)):
		print category[index]
		for index2 in range(len(list_product[index])):
			print list_product[index][index2][0],": $",list_product[index][index2][1]
		print '----------'	
		
	add = raw_input('What would you like to buy (enter name) ?');
	
	price = products[add.lower()]
	global your_cart 
	your_cart.append([add, price]);
	
	cart()
	
def cart():
	global your_cart
	print '----------'
	if len(your_cart) > 0:
		print 'Your cart: '
		for index in range(len(your_cart)):
			print your_cart[index][0],'$',your_cart[index][1]
	else:
		print 'Cart is empty'
	print '----------'
	raw_input('press any key to back to menu');
	menu()
	
def checkout():
	global your_cart
	global total
	
	for index in range(len(your_cart)):
		total = total + your_cart[index][1]
			
	if total > 0 :		
		print '----------'	
		print 'Your cart: '
		for index in range(len(your_cart)):
			print your_cart[index][0],'$',your_cart[index][1]
		print '----------'
		print 'Your total is $',total
		print '----------'
		print 'Thank you for shopping with us'
		print '----------'
		your_cart = []
		total = 0
	else:
		print '----------'
		print "**** Can't check out because you don't have anything in your cart ****"
		print '----------'
		
	raw_input('press any key to back to menu');	
	menu()
	
def empty_cart():
	global your_cart
	global total
	your_cart = []
	total = 0
	print '----------'
	print 'Cart has been emptied'
	print '----------'
	raw_input('press any key to back to menu');
	menu()
	
		
def menu():	
	print '----------'
	print 'Main Menu'
	print '----------'
	print '1. View & Buy Item'
	print '2. View Cart'
	print '3. Checkout'
	print '4. Empty Cart'
	print 'Enter anything to exit'
	c = raw_input('Choose : ');
	
	if c == '1':
		items()
	elif c == '2':
		cart()
	elif c == '3':
		checkout()
	elif c == '4':
		empty_cart()
	else:
		exit()

