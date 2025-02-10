import os

folder_list= input("Please provide the list of folders names with spaces in between:").split()

for folder in folder_list:
    
    try:
      files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide the correct folder name,which is not present in the current directory", folder)
        break
    except PermissionError:
        break
    print("===============listing files for the folder- " + folder)
    
    for file in files:
        print(file)