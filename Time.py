import time;
ticks=time.time()

print "The Current Time is :",ticks

localtime = time.localtime(time.time())
print "The local timing is :",localtime

i=1
while i :
	localtime1 = time.asctime(time.localtime(time.time()))
	print "The local timing is :",localtime1