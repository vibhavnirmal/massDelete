import os

dirname = input("Enter the directory path")
def rename():
    file_list = os.listdir(dirname)
    print(file_list)
    saved_path = os.getcwd()
    
    os.chdir(dirname)
    for file_name in file_list:
        os.rename(file_name,)
    os.chdir(saved_path)

rename()
