def ReverseString(name):
    size = len(name)

    if size == 0:
        return 0

    lastchar = name[size-1]
    print(lastchar,'')
    return ReverseString(name[0:size-1])

Name = input("Enter Name : ")

ReverseString(Name)