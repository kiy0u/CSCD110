# Section 3, October 2, 2023, Assignment 1

num1 = int(input("Enter a number that is not zero:"))

num2 = int(input("Enter another number that is not zero:"))

total_add = num1 + num2

total_sub = num1 - num2

total_mult = num1 * num2

total_sq = num1 ** num2

total_div = num1 // num2

print(num1, "plus", num2, "equals", total_add)               

print(num1,"minus", num2, "equals", total_sub)

print(num1,"multiplied by", num2, "equals", total_mult)

print(num1, "raised to the", num2,"equals", total_sq)

print(num1, "divided by", num2, "equals", total_div, "with a remainder of", num1 % num2)
