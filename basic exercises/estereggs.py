loaf_price = price_per_kilo_flour + pack_eggs_price + litter_milk_price * 0.250

money_left = budget
coloured_eggs = 0
loaf_counter = 0
lost_eggs = 0

while money_left > loaf_price:
    money_left -= loaf_price
    loaf_counter += 1
    coloured_eggs += 3
    if loaf_counter % 3 == 0:
        lost_eggs = loaf_counter - 2
        coloured_eggs -= lost_eggs

print(
    f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs} eggs and {money_left:.2f}BGN left.")