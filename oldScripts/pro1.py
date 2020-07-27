#Pro1 / by 7 but !* 5 range(2000,3201)

n,count=0,0
for i in range(2000,3201):
    if(i%7 == 0 and i%5 != 0):
        if(count < n):
            print(",",end="")
            count=count+1
        print(i,end="")
        n=n+1
    
print("\n\nTotal Numbers are ",n)
