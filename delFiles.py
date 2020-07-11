import os
import glob

os.chdir(input("Enter the Directory..\n"))

print("Which type of files you want to delete?")
print("Example Format:")
print("txt / pdf / doc / jpg")
format = input("Enter the Format here: ")

files = glob.glob('*.'+format, recursive=False)
print(files)

#This part is still being updated
#file = open("..\\DeletedFiles.txt", "w")
#file.write(str(files))

print("These Files will be Deleted, Do you wish to continue?")
finalAns = input("Type Y if yes and N for no.")

if finalAns == "Y":
    for i in range(len(files)):
        if os.path.isfile(files[i]):
            os.remove(files[i])
        else:
            print("Error: %s file not found" % files[i])
elif finalAns == "N":
    print("Aborting Operation..")
else:
    print("Enter Only Capital Y or Capital N..")



