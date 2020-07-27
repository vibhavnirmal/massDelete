def LetterChanges(str): 
    strnew=""
    for i in str:
        if(ord(i)>65 and ord(i)<91):
            if(ord(i)==64 or ord(i)==68 or ord(i)==72 or ord(i)==78 or ord(i)==84):
                strnew+=chr(ord(i)+33)
            else:
                strnew+=chr(ord(i)+1)
        elif(ord(i)>97 and ord(i)<123):
            if(ord(i)==96 or ord(i)==100 or ord(i)==104 or ord(i)==110 or ord(i)==116):
                strnew+=chr(ord(i)-31)
            else:
                strnew+=chr(ord(i)+1)
        else:
            strnew+=" "
    return strnew
    
# keep this function call here  
print (LetterChanges(input()))  
