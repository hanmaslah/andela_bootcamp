def prime(k):
"""
This is a method to print the numbers in the range provided
and prints whether prime or not prime 
"""
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not a prime number")
				break
		else:
			print(k, "is a prime number")
	else:
		return None 
	prime(k-1)
