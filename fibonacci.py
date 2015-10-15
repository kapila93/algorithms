#FIBONACCI SERIES
series = [0, 1]
my_range = int(raw_input())
if my_range == 1:
	print 0;
else:
	while(len(series) < my_range):
		series.append(series[len(series) - 2] + series[len(series) - 1])

	for value in series:
		print value