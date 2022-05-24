command = ""
coffes_needed = 0
while command.lower() != "end":
    command = input()

    if command.lower() == "coding" or command.lower()== "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffes_needed += 1
        else:
            coffes_needed += 2
if coffes_needed > 5:
    print("You need extra sleep")
else:
    print(coffes_needed)


