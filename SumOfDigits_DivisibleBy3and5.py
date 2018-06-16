#Program to find the sum if digits which are divisible by 3 and 5
#Assigning sum value to zero
sum=0

#Finding the number divisible by 3 and 5 within 1000
#And printing the Sum
for i in range(0,1000):
	if i%3==0 or i%5==0:
		sum=sum+i
print(sum)