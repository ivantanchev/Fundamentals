string = str(input())


while string != "End":
    if string == "SoftUni":
        string = str(input())
    else:
        final = ""
        for char in string:
            final += char*2
        string = str(input())
        print(final)

