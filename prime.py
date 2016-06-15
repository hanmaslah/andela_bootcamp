def prime(n):
    """
This method returns a list of the first n prime numbers
The method takes in an integer and prints a list with the length of the integer
provided which will be a list of the first n prime numbers
    """
        
    primes =[2]
    curr=2
    if n<1:
                return "the list of prime numbers cannot be less than 1"
    while True:
        isprime=True
        for prime in primes:
            if curr%prime==0:
                isprime=False
                break
        if isprime: 
            primes.append(curr)
        curr+=1
        if len(primes)==n:
            break
    print( "The first", n, "prime numbers are: \n", primes)



    
