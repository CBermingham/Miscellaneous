import random

minimum = int(raw_input("Lowest number in range: "))
maximum = int(raw_input("Highest number in range: "))
number = random.randint(minimum, maximum)

statement = "Guess a number between " + str(minimum) + " and " + str(maximum) + ": "
guess = int(raw_input(statement))
tries = 0
while guess != number:
	if guess > maximum or guess < minimum:
		print "Number out of range"
	elif guess < number:
		print "Too low"
	elif guess > number:
		print "Too high"
	guess = int(raw_input(statement))
	tries +=  1


print "Correct number!"
print "Number of tries: ", tries + 1
