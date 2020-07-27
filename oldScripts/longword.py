def LongestWord(sentence):
    maxcount=0
    for letter in sentence.split(" "):
        if(len(letter)>maxcount):
            maxcount=len(letter)
            final = letter
        else:
            pass

    return final

print(LongestWord(str(input())))
