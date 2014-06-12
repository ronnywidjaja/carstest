def binary():
	n = input('enter number:')
	while n>0:
		print n%2,
		if (n%2)==1:
			n-=1
		n=n/2
