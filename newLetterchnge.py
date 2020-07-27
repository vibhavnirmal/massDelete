def LetterChanges(str): 
    strnew=""
    for i in str:
        if(ord(i)>=65 and ord(i)<91):
            if(ord(i)==64 or ord(i)==68 or ord(i)==72 or ord(i)==78 or ord(i)==84):
                strnew+=chr(ord(i)+33)
            elif(ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85):
                strnew+=chr(ord(i)+1)
            else:
                strnew+=chr(ord(i)+1)
        elif(ord(i)>=97 and ord(i)<123):
            if(ord(i)==96 or ord(i)==100 or ord(i)==104 or ord(i)==110 or ord(i)==116):
                strnew+=chr(ord(i)-31)
            elif(ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117):
                strnew+=chr(ord(i)+1)
            else:
                strnew+=chr(ord(i)+1)
        elif(i == " "):
            strnew+=" "
        else:
            strnew+=i
    return strnew
    
# keep this function call here  
print (LetterChanges(input()))  
















  
