string=input("Enter the String\n")

cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8,cnt9,cnt10,cnt11,cnt12,cnt13,cnt14,cnt15,cnt16=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
for i in string:
    if(i=="#"):
        cnt1+=1
    elif(i=="%"):
        cnt2+=1
    elif(i=="$"):
        cnt3+=1
    elif(i=="^"):
        cnt4+=1
    elif(i=="*"):
        cnt5+=1
    elif(i=="&"):
        cnt6+=1
    elif(i=="@"):
        cnt7+=1
    elif(i=="!"):
        cnt8+=1
    elif(i=="("):
        cnt9+=1
    elif(i==")"):
        cnt10+=1
    elif(i=="_"):
        cnt11+=1
    elif(i=="+"):
        cnt12+=1
    elif(i=="{"):
        cnt13+=1
    elif(i=="}"):
        cnt14+=1
    elif(i=="["):
        cnt15+=1
    elif(i=="]"):
        cnt16+=1
        
print ("# ",cnt1)
print ("% ",cnt2)
print ("$ ",cnt3)
print ("^ ",cnt4)
print ("* ",cnt5)
print ("& ",cnt6)
print ("@ ",cnt7)
print ("! ",cnt8)
print ("( ",cnt9)
print (") ",cnt10)
print ("_ ",cnt11)
print ("+ ",cnt12)
print ("{ ",cnt13)
print ("} ",cnt14)
print ("[ ",cnt15)
print ("] ",cnt16)
