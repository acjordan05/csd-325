"""
Author: Aysa Jordan
Date: November 20, 2025
Assignment: Module 7.2
"""

"""
This program defines a simple function named city_country() that takes a city name and a country name and returns them in 
the format “City, Country.” At the bottom of the file, the function is called three times so one can run the 
program and show the output.
"""

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

# Call the function at least 3 times
print(city_country("santiago", "chile"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))
