def prime(k):
	
		for n in range (2,k):
			if k>1:
				for i in range (2,n):
					if n%i==0:
						print (n, "is not prime")
						print(i, "times", n//i, "is", n)
						break
				else:
					print(n, "is prime")
