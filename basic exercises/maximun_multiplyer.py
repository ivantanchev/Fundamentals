devisor = int(input())
bounder= int(input())

for current_number in range(bounder,devisor, -1):
    if current_number % devisor == 0:
        break
print(current_number)
