def fact(x):
	if x<0:
		return "No fact for negatives"
	elif x==0:
		return 1
	else:
		return x*fact(x-1)
import math
#using the inbuilt factorial method
math.factorial (5)
