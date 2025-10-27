"""
Author: Aysa Jordan
Date: October 26, 2025
Assignment: Module 2.2
"""

"""
This program prompts the user to enter two numbers, adds them together using a function add_numbers, 
and prints the sum.
"""

# simple_math.py
def add_numbers(a, b):
    return a + b

def main():
    print("Simple Math Program")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_numbers(x, y)
    print("The sum is:", result)

if __name__ == "__main__":
    main()

# result = add_numbers(x, y) #