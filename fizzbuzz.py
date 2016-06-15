def fizz_buzz(n):
    """
Return fizz when n is divisible by 3
Return buzz when n is divisible by 5
Return fizzbuzz when n is divisible by both 3 and 5
    """
    if not isinstance (n , int):
        return 'Kindly enter a digit'
    elif n % 3 == 0 and n % 5  == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n
