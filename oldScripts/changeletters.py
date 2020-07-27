string=input("Enter the String\n")

y= string.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
print (string.translate(y))

#for i in string:
 #   if(i=="y"):
 #       print ("a",end="")
 #   elif(i=="z"):
 #       print ("b",end="")
 #   elif(i==" "):
 #       print (" ",end="")
 #   elif(i=="."):
 #       print (".",end="")
 #   else:
 #      print (chr(ord(i)+2),end="")

#for i in string:
#    if(int(ord(i))>96 and int(ord(i))<120):
#        print (chr(ord(i)+2),end="")
#    elif(i=="y"):
#        print ("a",end="")
#    elif(i=="z"):
#       print ("b",end="")
#    else:
#        print (i,end="")
