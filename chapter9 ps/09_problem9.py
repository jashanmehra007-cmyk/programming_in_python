with open("this.txt") as f:
    content1 = f.read()

with open("log.txt") as f:
    content2 = f.read()

    if content1 == content2:
        print("YES FILES ARE IDENTICAL")
    else:
        print("NO FILES ARE NOT IDENTICAL")
        