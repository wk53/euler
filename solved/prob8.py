"""Project Euler - Problem 8.

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

(1000-digit number stored in prob8.txt)

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""

import re

f = open("prob8.txt", "r")
number = re.sub("[^0-9]", "", f.read())  # remove non-numeric chars

greatest_product = 0

for i in range(len(number) - 13):
    product = 1  # prevent multiply by 0 error
    for j in range(13):
        product *= int(number[i + j])
    if product > int(greatest_product):
        greatest_product = int(product)

print(greatest_product)
