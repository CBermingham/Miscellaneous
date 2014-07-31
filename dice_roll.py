import random
import matplotlib.pyplot as plt

def roll():
	number = round(random.random() * 6 + 0.5) #generate a random number from 1 to 6
	return number

maximum = int(raw_input("Number of rolls: "))


frequency = [0]*6

for i in range (0, maximum):
	num = roll()
	for j in range (1, 7):
		if num == j:
			frequency[j-1] = frequency[j-1] + 1

x_vals = range(1, 7)
x_vals = [i - 0.5 for i in x_vals]

plt.bar(x_vals, frequency)
plt.show()





		
