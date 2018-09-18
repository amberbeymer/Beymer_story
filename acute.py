pyth_diff = a[2]**2 - (b[0]**2 + c[1]**2)
if (pyth_diff > 0):
	print("Triangle is obtuse")
elif (pyth_diff == 0):
	print("Triangle is right")
else:
	print("Triangle is acute")