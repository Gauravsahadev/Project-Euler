#Finding the sum of even valued terms in fibonacci series within 4million
#Assigning sum and EvenSum initial value
Fsum=0
evenSum=2
#Assigning a and b value
a=1
b=2

#Fibonacci Series to 4million 
#Printing even Sum to 4million
while(b<=4000000):
	Fsum=a+b
	a=b
	b=Fsum
	print(Fsum)
	if b%2==0:
		evenSum=evenSum+b
print(evenSum)