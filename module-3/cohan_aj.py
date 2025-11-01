"""
Cho-Han Modified by Aysa Jordan
Assignment: Module 3.2
Based on original by Al Sweigart
Date: November 1, 2025
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han Modified by Aysa Jordan

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Note: If the total roll is a 2 or a 7, you earn a 10 mon bonus!
''')

purse = 5000

while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('aj: ')  # Changed input prompt to initials
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('aj: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won
    rollTotal = dice1 + dice2
    rollIsEven = (rollTotal % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        house_fee = pot * 0.12  # Changed from 10% to 12%
        print('The house collects a', int(house_fee), 'mon fee.')
        purse = purse - int(house_fee)

        # BONUS condition
        if rollTotal == 2 or rollTotal == 7:
            print(f'Bonus! You rolled a {rollTotal} and earned 10 mon!')
            purse += 10

    else:
        purse = purse - pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
