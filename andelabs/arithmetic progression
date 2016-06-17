def arith_geo(mylist):
    if len(mylist) != 0:
        geometric = []
        arithmetic = []
        for i in range(len(mylist) - 1):
            if mylist[i + 1] == 0 or mylist[i] == 0:
                geometric.append(0)
            else:
                geometric.append(mylist[i + 1] / float(mylist[i]))
            arithmetic.append(mylist[i + 1] - mylist[i])
        geometric = set(geometric)
        arithmetic = set(arithmetic)
        if len(geometric) == 1:
            return 'Geometric'
        elif len(arithmetic) == 1:
            return 'Arithmetic'
        else:
            return -1
    return  0


