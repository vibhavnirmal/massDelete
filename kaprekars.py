def KaprekarsConstant(num): 
    count=0
    for i in range(100):
        if( int(num) != 6174):
            if(len(num)!=4):
                num = num+"0"
            else:    
                x="".join(sorted(num))
                y=x[::-1]
        
                if(int(x)>int(y)):
                    num=str(int(x)-int(y))
                    print (num,count)
                else:
                    num=str(int(y)-int(x))
                    print (num,count)
                count+=1

    return count

print (KaprekarsConstant(input()))
