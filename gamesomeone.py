import random
import math
import sys

comand = " "
curent_money = 0
print("Има торба пълна с портмонета с различни суми пари.")
print("Не знаете каква е максималната сума в портмоне и броя на портмонетата.")
print("Бъркате и вадите едно портмоне.")
print("Ако ви хареса сумата, не продължавате и вземате тази сума.")
print("Ако смятате, че може да изтеглите по висока сума, продължавате с 'y'.")
print("Не може да се връщате към предишна сума.")
print("При изчерпване на портмонетата оставате с последното.\n")
max_money = random.randint(1, sys.maxsize) / 100000000000000
max_money = int(max_money)

comand = input("Изтеглете първото портмоне: ")
if comand == "y":
    curent_money = random.randint(1, max_money)
while comand == "y":
    curent_money = random.randint(1, max_money)
    print(f"{curent_money}")
    comand = input("Ще продължите ли? ")
percent = curent_money / max_money * 100
print(f" Вие взехте {curent_money} от {max_money} или {percent:.0f}% от максималната сума.")