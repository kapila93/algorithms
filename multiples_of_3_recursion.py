# multiples of 3 function in recursion

def multiply(n):
	if n != 0:
		product = (3 * n)
		print product
		multiply(n - 1)

some_number = 433
multiply(some_number)