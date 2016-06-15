def prime(num):
    """
This method returns a list of the first n prime numbers
The method takes in an integer and prints a list with the length of the integer
provided which will be a list of the first n prime numbers
It was to print whether a number is prime or not but for the sake of conflict,
had to change the code 
    """
        
    primes =[2]
    curr=2
    if num<1:
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
        if len(primes)==num:
            break
    print( "The first", num, "prime numbers are: \n", primes)



    
