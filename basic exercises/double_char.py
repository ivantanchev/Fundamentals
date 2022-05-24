string = str(input())
final = ""
while string != "End":
    for char in string:
        final += char*2
        string = str(input())
    print(final)

