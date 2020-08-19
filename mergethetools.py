import math
a=input()
n=int(input())
m=n
length=len(a)
num=math.ceil(length/n)
s=[]
print(num,length)
for i in range(num):
	c=a[m-n:m]
	s.append(c)
	m+=n
l1=[]
l2=[]
for i in range(len(s)):
	for j in range(n):
		l1.append(s[i][j])
	l1= list(dict.fromkeys(l1))
	l2.append(list(l1))
	l1.clear()
for i in l2:
	x="".join(i)
	l1.append(x)
for i in l1:
	print(i)