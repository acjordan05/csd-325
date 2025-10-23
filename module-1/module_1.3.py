""""
Author: Aysa Jordan
Date: October 23, 2025
Assignment: Module 1.3
"""

"""
This program asks the user for a number of bottles and then counts down while printing the lyrics 
to "Bottles of Beer on the Wall."
"""

def beer_countdown(bottles):
    # Loop until bottles reach 0
    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        bottles -= 1

def main():
    # Ask the user for input
    num_bottles = int(input("Enter number of bottles: "))
    print()  # blank line for readability
    beer_countdown(num_bottles)
    print("Time to buy more bottles of beer.")

# Run the program
if __name__ == "__main__":
    main()

# SOURCES
# Programs written in CSD 205
# W3Schools.com. (n.d.). https://www.w3schools.com/Python