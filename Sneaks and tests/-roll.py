import random



# Ask for input
die_com = input(": ")


# Check if the user used the command
if "-roll" == die_com[0:5]:
	print("Rolling " + str(die_com[6:10]) + "...")
	

	# Check the amount of dices
	if "1" in die_com[6]:
		roll = 1
	elif "2" in die_com[6]:
		roll = 2
	elif "3" in die_com[6]:
		roll = 3
	elif "4" in die_com[6]:
		roll = 4
	elif "5" in die_com[6]:
		roll = 5
	elif "6" in die_com[6]:
		roll = 6 # I guess that we dont need more
	elif "d" in die_com[6]:
		roll = 1 # The user did not input a number for the amount of dices, so we guess that he wants only one
	else:
		print("Please use a number from 1-6 for the amount of dices!")


	# Check the die (4, 6, 8, 10, 12 or D20)
	if "d4" in die_com[6:10]: # Why are we using 6:10 instead of 7:10? Well our user might not input an number for the amount of dices
		die = 4
	elif "d6" in die_com[6:10]:
		die = 6
	elif "d8" in die_com[6:10]:
		die = 8
	elif "d10" in die_com[6:10]:
		die = 10
	elif "d12" in die_com[6:10]:
		die = 12
	elif "d20" in die_com[6:10]:
		die = 20
	else:
		print("Please use d4, d6, d8, d10, d12 or d20. There are no other 'regular' dices.")


	# Do some math
	res = 0 # Just in case...
	i = 0	# Our counter for the loop
	while i < roll:
		res1 = random.randint(1, die)
		res += res1
		i += 1
		# Debug
		#print("Rolled a " + str(res1))
		#print ("Score is now " + str(res))


	# Debug
	#print(" ")
	#print("Debug:")
	#print("Dies-->" + str(roll))
	#print("Die-->" + str(die))
	#print("------")

	# Print out the result
	print("Result-->" + str(res))

	# Use this in case the player does not input any data beside the "-roll" command:
	#	print("Please use the command like this: '-roll 3d12' or just '-roll d12'")

