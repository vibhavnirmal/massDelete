#pro5 Class getstring printstring methods

class String:
    def __init__(self):
        self.string = ""

    def getstring(self):
        self.string= input()
        
    def printstring(self):
        print (self.string.lower())
        
string=String()

string.getstring()
string.printstring()
