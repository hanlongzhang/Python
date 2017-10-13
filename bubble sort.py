arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
	for j in range(i+1):
		if arays[i]<arays[j]:
			arays[i],arays[j] = arays[j],arays[i],
			print arays
print arays