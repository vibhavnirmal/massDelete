def SimpleAdding(num): 
    if(num == 0):
        return 0
    return num+SimpleAdding(num-1)

print (SimpleAdding(int(input())))
