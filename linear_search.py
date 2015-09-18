# LINEAR SEARCH

someListofNumbers=[4,14,13,28,3,15,83,23]
print someListofNumbers
print ""

valueToFind = 28
lengthOfList = len(someListofNumbers)

counter = 0

while counter < lengthOfList:
	if someListofNumbers[counter] == valueToFind:
		print "Value is position %s in the list of numbers" % (counter + 1)
		break
	elif counter == lengthOfList - 1:
		print "NIL"
		break
	else:
		counter = counter + 1
