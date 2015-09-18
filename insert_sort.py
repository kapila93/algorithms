someListofNumbers=[4,14,13,28,3,15,83,23]
print someListofNumbers
print ""
lengthOfList = len(someListofNumbers)

j = 1
for j in range (0, lengthOfList):
	key = someListofNumbers[j]
	i = j - 1
	while i >= 0 and someListofNumbers[i] > key:
		someListofNumbers[i + 1] = someListofNumbers[i]
		i = i - 1
	someListofNumbers[i + 1] = key
	j = j + 1
print someListofNumbers
