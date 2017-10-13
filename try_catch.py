try:
	fh=open("testfile","w")
	fh.write("this is a test file,use test unnormal!!")
escept IOError:
	print "Error: No search file or read/write fail"
else:
	print"Write file OK"
	fh.close()
	