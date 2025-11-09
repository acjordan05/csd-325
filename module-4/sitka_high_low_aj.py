"""
Sitka_Highs Modified by Aysa Jordan
Assignment: Module 4.2
Date: November 9, 2025
This program displays a menu to show either high or low daily temperatures
for Sitka weather data, or exit the program.
"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys  # used to exit the program cleanly

filename = 'sitka_weather_2018_simple.csv'

def read_weather_data(filename):
    """Read weather data from CSV and return lists of dates, highs, and lows."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_weather(dates, temps, temp_type='High'):
    """Plot the temperatures as a line chart."""
    fig, ax = plt.subplots()
    color = 'red' if temp_type.lower() == 'high' else 'blue'
    ax.plot(dates, temps, c=color)

    plt.title(f"Daily {temp_type} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    dates, highs, lows = read_weather_data(filename)

    print("Welcome to the Sitka Weather Viewer!")
    while True:
        print("\nMenu Options:")
        print("1. Highs")
        print("2. Lows")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            plot_weather(dates, highs, 'High')
        elif choice == '2':
            plot_weather(dates, lows, 'Low')
        elif choice == '3':
            print("Thank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()