# Given a column title as appear in an Excel sheet, return its corresponding column number.
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example:
# Input: "ZY"
# Output: 701

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
li=[]

def findNum(S):
    for i in S:
        for i, j in enumerate(string):
            if j == i:
                li.append(i+1)
    final = 0
    for i, j in enumerate(li):
        final = final + (26**(len(li) - i - 1))*j
    return final

print(findNum(input("Enter String: \n")))