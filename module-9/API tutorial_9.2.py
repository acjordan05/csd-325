"""
Author: Aysa Jordan
Date: November 26, 2025
Assignment: Module 9.2
"""

"""
This program retrieves data from the Open Notify API and displays a formatted list of
astronauts currently in space along with their spacecraft.
"""

import requests
import json

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

# ---------- FORMATTED JSON OUTPUT ----------
print("\n=== FORMATTED JSON DATA ===")
formatted = json.dumps(response.json(), indent=4)
print(formatted)

# ---------- FORMATTED ASTRONAUT LIST ----------
data = response.json()

print("\n=== CURRENT ASTRONAUTS IN SPACE ===")
print(f"There are currently {data['number']} astronauts in space:\n")

for person in data["people"]:
    print(f"{person['name']} aboard {person['craft']}")

# SOURCE
# Custer, C. (2025, November 13). How to use an API in Python. Dataquest. https://www.dataquest.io/blog/api-in-python/