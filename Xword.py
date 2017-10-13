rows = int(raw_input("input line:"))
i=1
while i<=rows:
	if i<=rows/2:
		print("*"*i)
		
	elif i<=rows:
		j=i-2*(i-rows/2)
		print("*"*j)
	i+=1
else:
	print("")