def appen(num,dec):
	numbers = []
	for i in range(0, num, dec):
		print "At the top i is %d" % i 
		
		numbers.append(i)
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"

	for num in numbers:
		print num


appen(10,2)