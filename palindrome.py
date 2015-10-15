#PALINDROME
print "Input a string to check if it is a palindrome:"
my_string = raw_input()

if my_string == my_string[::-1]:
	print "'%s' is a palindrome!" % my_string
else:
	print "'%s' is not a palindrome!" % my_string