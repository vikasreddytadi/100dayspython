n=13
m=39
n1=n//2
z=0
c=3
l=[".","|","."]
for i in range(1,n1+1):
	for j in range(1,m+1):
		if(j<=n1*c-3*(i-1)):
			print("-",end="")
		elif(j>n1*c-3*(i-1) and j<=n1*c+3*(i)):
			print(l[z],end="")
			z+=1
			if(z>2):
				z=0
		else:
			print("-",end="")
	print(" ")
x=(m-7)//2
y="-"
print(y*x,end="")
print("WELCOME",end="")
print(y*x)
z=0
for i in range(1,n1+1):
	for j in range(1,m+1):
		if(j<=3*i):
			print("-",end="")
		elif(j>3*i and j<=m-3-3*(i-1)):
			print(l[z],end="")
			z+=1
			if(z>2):
				z=0
		else:
			print("-",end="")
	print(" ")
		
			