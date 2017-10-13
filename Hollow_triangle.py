#coding:utf-8
rows = int(raw_input("input line:"))
for i in range(0,rows):
	for k in range(0,2*rows-1):
		if (i!=rows-1)and(k==rows-i-1 or k==rows+i-1):
			print "*",
		elif i == rows-1:
			if k%2 == 0:
				print '*',
			else:
				print "!",
		else:
			print "$",
	print "\n"