def prime(n):
    """
this functions takes a number and prints if it is a prime or not
and if not, it prints the first factors

    """
	if n>1:
		for i in range (2,n):
			if n%i==0:
				print (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				print(n, "is prime")



    
