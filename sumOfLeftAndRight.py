#find index from which sum of left and right side is same

x = [1,100,50,-51,1,1]

def find_index(x):
    s = 0
    for i in range(0, len(x)):        
        if sum(x[p] for p in range(0, i)) == sum(x[q] for q in range(i+1, l)):
            print(i)

find_index(x)
