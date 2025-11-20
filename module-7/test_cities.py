"""
Author: Aysa Jordan
Date: November 20, 2025
Assignment: Module 7.2
"""

"""
This program uses Python’s unittest library to test whether the city_country() function returns the correct formatted 
string when given “santiago” and “chile.” If the function works correctly, the test will pass.
"""

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
