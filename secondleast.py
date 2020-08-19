d={"vikas":50,"sowji":70,"jagan":80}
l=[]
for i in d:
	l.append(d[i])
l.sort()
c=min(l)
for i in l:
	if(i==c):
		continue
	else:
		c=i
		break
for i in d:
	if(d[i]==c):
		print(i)