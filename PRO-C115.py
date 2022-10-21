import os
source = "PRO-C115Text.txt"
dest = "New_file_name.txt"
os.rename(source, dest)
print("renamed the file")