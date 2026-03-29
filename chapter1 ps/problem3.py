import os # Operating system built in module(no pip install needed!)
#Talks to your Windows
# lists files/folders
# Gets file sizes, dates
# Checks if file/folder exists
# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
