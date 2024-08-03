from functools import reduce
solution = lambda nl: 1 if  reduce(lambda x,y: x*y, nl, 1) < sum(nl)**2 else 0
