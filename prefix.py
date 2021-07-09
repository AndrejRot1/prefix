# Very important to use whail insted of for to create prefixes because if u run with for one by one u cant get [0:n]. Its
# just one character

def check(book):
	prefixes = []
	results = []
	c = 1
	alfa = False
	while(c <= len(book[0])):
		prefix = book[0][0:c]
		if c > len(book[0]):
			break
		prefixes.append(prefix)
		c = c + 1
	c = 1
	for prefix in prefixes:
		for index in range(1,len(book)):
			if (prefix == book[index][0:c]) == True:
				alfa = True
			else:
				alfa = False
		if alfa == True:
			results.append(prefix)
		c = c + 1
	return results