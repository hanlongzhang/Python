dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
	flag = raw_input("Add or Find words?(a/c)")
	if flag == 'a':
		word = raw_input("input words(key):")
		defintion = raw_input("input define Val(Value):")
		dictionary[str(word)] = str(defintion)
		print "Add Ok!"
		pape = raw_input("Do you want find Dictionary?(a/0)")
		if pape == 'a':
			print dictionary
		else:
			continue
	elif flag == 'c':
		check_word = raw_input("Find you words:")
		for key in sorted(dictionary.keys()):
			if str(check_word) == key:
				print "This Word Exist!",key,dictionary[key]
				break
			else:
				off = 'b'
			if off == 'b':
				print "Sorry,This value Don't Exist!"
		else:
			print "error type"
			break