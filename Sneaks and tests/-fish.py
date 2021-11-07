import random

i = random.randint(1, 12)
print (i)

if i >= 1 and i <= 3:
	print ("O one")
elif i >= 4 and i <= 5:
	print ("O two")
elif i >= 6 and i <= 8:
	print ("O three")
elif i >= 9 and i <= 11:
	print ("O four")
elif i == 12:
	print ("O five")
else:
	print ("Error!")
