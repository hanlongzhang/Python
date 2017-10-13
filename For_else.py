for num in range(10,20):
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			print '%d be equal to %d * %d' %(num,i,j)
			continue
	else:
		print num,'is a prime number'