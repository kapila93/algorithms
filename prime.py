#IS IT A PRIME NUMBER?
import math

def check_prime(some_number):
	if some_number <= 3:
		return True;
	elif (some_number % 2) == 0:
		return False;
	else:
		for counter in range(3, int(math.sqrt(some_number)) + 1, 2):
			if (some_number % counter) == 0:
				return False
	return True

print "Enter a number to check if it's a prime number or not:"
my_number = int(raw_input())

if check_prime(my_number) == True:
	print "%s is a prime number!" % my_number
else:
	print "%s is not a prime number!" % my_number