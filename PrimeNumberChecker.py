number = int(input("Please enter a number: "))

is_prime = True;

for factor in range(2, number):
	if number % factor == 0:
		is_prime = False;
		break

if is_prime == True:
	print("%d is a prime number!") % number
else:
	print("%d is NOT a prime number!") % number 