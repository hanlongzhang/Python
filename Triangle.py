for i in range(1,11):
	for k in range(1,i+1):
		n = i*k
		print '%d*%d=%d' %(k,i,n),
		k +=1
	i +=1
	print "\n"