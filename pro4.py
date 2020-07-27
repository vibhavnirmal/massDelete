#pro4 list and tuple

n= int(input("How many No.s you Want "))

lst= []
t= tuple()
for i in range (1,n+1):
     print("Elemnt",i,"in list",end=" ")
     lst.append(str(input()))
     print("Elemnt",i,"in Tuple",end=" ")
     t=t+(tuple(str(input())))

print(lst)
print(t)


#value=input()
#I=value.split(",")
#t=tuple(I)

#print(I)
#print(t)
