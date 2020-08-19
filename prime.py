n=int(input("entet a number"))
count=0
for i in range(2,n):
	if(n%i==0):
		count+=1
		break
if(count==0):
	print(n,"is a prime number")
else:
	print(n,"is not a prime number")