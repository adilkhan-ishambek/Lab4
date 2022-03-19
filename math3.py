import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
num = a*a*math.sin(2/n*math.pi)
den = 8*(math.sin(math.pi/n)**2)
print(round((n*num)/den, 1))