def LetterChanges(String): 
    strnew = ""
    for i in String:
        strnew+=chr(ord(i)+1)
    
    return strnew
    
# keep this function call here  
print (LetterChanges(input()))
















  
