def apen(num,dec):
	i = 0 
	numbers = []
	while i < num :
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + dec
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"
	for num in numbers:
		print num


apen(10,2)