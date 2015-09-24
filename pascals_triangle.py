# pascal's triangle

def pascal(power):
	row = [1]
	pwr_count = 1
	print row
	pascalrow(row, pwr_count, power)

def pascalrow(row, pwr_count, power):
	if pwr_count < power:
		# print "setting new row to original row now"
		new_row = list(row)
		
		for index in range(0, pwr_count):
			# print "Loop # %s" % index
			# print "original row %s" % row
			if index == 0:
				# print "appended 1"
				new_row.append(1)
			elif index > 0 and index < len(new_row):
				new_row[index] = row[index-1] + row[index]
			else:
				print "Nothing happened."
			# print "New Row %s" % new_row
			# print "End of Loop # %s" % index
			# print ""

		# print "after the loop %s" % new_row
		print new_row
		# print ""
		pwr_count = pwr_count + 1
		pascalrow(new_row, pwr_count, power)


pascal(10)


# 0 = 0
# 1 = 0 + 1
# 2 = 1 + 2
# 3 = 2 + 3
# 4 = 3 + 4

# n = (n-1) + n