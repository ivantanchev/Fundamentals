number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_of = float(input())
    days = int(input())
    capsule_per_day = int(input())


    if price_of < 0.01 or price_of > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day >2000:
        continue
    curent_total = capsule_per_day * days* price_of
    total_price += curent_total
    print(f"The price for the coffee is: ${curent_total:.2f}")
print(f"Total: ${total_price:.2f}")
