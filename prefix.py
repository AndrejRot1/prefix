# Very important to use whail insted of for to create prefixes because if u run with for one by one u cant get [0:n]. Its
# just one character

def check(book):
	results = []
	c = 1
	while(c <= len(book[0])):
		prefix = book[0][0:c]
		if c > len(book[0]):
			break
		# print(prefix)
		for index in range(1,len(book)):
			if prefix == book[index][0:c]:
				results.append(prefix)
			else:
				return 'no prefix'
		c = c + 1
	return max(results)