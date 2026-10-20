def hammy():
	a = input('Please input the first string: ')
	b = input('Please input the second string: ')
	hamming = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			hamming += 1
	return hamming

print(hammy())



