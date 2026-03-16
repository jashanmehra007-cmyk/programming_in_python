with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("The word 'python' is present in the file.") 
else:   
    print("The word 'python' is not present in the file.")