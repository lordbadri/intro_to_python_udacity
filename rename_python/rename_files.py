import os
def rename_files(path):
    file_list = os.listdir(path)
    print file_list
    original_path = os.getcwd()
    os.chdir(path)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print("old name - " +  file_name)
        print("new name - " + file_name.translate(None,"0123456789"))
    os.chdir(original_path)
path = r"D:/google_drive/Online courses/udacity/intro to python/rename_python/prank/" 
rename_files(path)
