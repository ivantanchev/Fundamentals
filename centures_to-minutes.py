from math import floor
centuries = int(input())
years = centuries * 100
days = years * 365.2422
hours = floor(days) * 24
minutes = hours * 60
print(f'{floor(centuries)} centuries = {floor(years)} years = {floor(days)} days = {floor(hours)} hours = {floor(minutes)} minutes')

