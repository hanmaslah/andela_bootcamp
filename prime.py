def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(k, "is prime")
	else:
		return None 
	prime(k-1)
