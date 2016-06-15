def fibonacci(n):
        """
A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8....
The terms are obtained by adding the preceding two terms.
This means to say the nth term is the sum of (n-1)th and (n-2)th term.
        """	
        a,b = 0,1
        print("Fibonacci series of",n,"terms is: ")
        for i in range(n):
				
                a,b = b,a+b
                
                print (a, end=' ')
