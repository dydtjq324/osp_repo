#!/usr/bin/python


fibonumber=int(input("생성할 피보나치 수는?:"))


a,b = 0,1
for i in range(fibonumber):
	a,b=b,a+b
	print(a)


print("F%d = %d" %(fibonumber,a))

