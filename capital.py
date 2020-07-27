import string

def LetterCapitalize(string):
    s=string #method 1: it will decapitalise letters inbetween
    print(string.title())
    s = ' '.join(word[0].upper() + word[1:] for word in s.split()) #method 2: it will remove the extra spaces 
    return s

print(LetterCapitalize(input()))
