import os
import glob

os.chdir(input("Enter the Directory..\n"))

print("Which type of files you want to delete?\n")
print("Example Format:\n")
print(" txt / pdf / doc / jpg / ini \n")
print("(Do not include dot(.), only write file format)\n")
theFormat = input("Enter the Format here: ")

files = glob.glob('*.'+theFormat, recursive=False)
print(files)

print("These Files will be Deleted, Do you wish to continue?")
finalAns = input("Type Y to continue and N to abort.")

if finalAns == "Y" or finalAns == "y":
    for i in range(len(files)):
        if os.path.isfile(files[i]):
            os.remove(files[i])
        else:
            print("Error: {} file not found".format(files[i]))
    
    fileN = open("..\\DeletedFiles.txt", "w")
    fileN.write(str(files))

elif finalAns == "N" or finalAns == "n":
    print("Aborting Operation..")
else:
    print("Invalid input.")
