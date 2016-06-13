def magic_sum(mylist):
    return sum([x//2 if x%2==0 else x*2 for x in mylist ])

