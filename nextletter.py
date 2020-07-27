def LetterChanges(str): 
    strnew = ""
    for i in str:
        strnew+=chr(ord(i)+1)
    
    return strnew
    
# keep this function call here  
print (LetterChanges(input()))
















  
