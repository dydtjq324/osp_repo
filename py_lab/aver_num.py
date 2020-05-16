#!/usr/bin/python

mysum=0



num=int(input("몇개의 숫자를 입력할래요?:"))

for i in range(num):
	num2=int(input("입력하세요:"))
	mysum+=num2



aver=mysum/num
print("평균 값은 %d입니다" %aver)


