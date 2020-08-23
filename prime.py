n=int(input("enter"))
m=int(input("enter"))
count=0
for i in range(n,m+1):
    for j in range(2,i):
        if(i%j==0):
            count+=1
        else:
            continue
    if(count==0):
        print(i,"prime")
    else:
        print(i,"not prime")
    count=0
    
