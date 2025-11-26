"""
Author: Aysa Jordan
Date: November 26, 2025
Assignment: Module 9.2
"""

"""
This program 
"""

import requests
import json

# New simple API (different from astronaut API)
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

# 1) CONNECTION TEST
print("\n=== CONNECTION STATUS ===")
print(response)  # should show <Response [200]>

# 2) RAW, UNFORMATTED API OUTPUT
print("\n=== RAW RESPONSE TEXT ===")
print(response.text)

# 3) FORMATTED JSON OUTPUT LIKE TUTORIAL STYLE
print("\n=== FORMATTED JSON OUTPUT ===")
formatted = json.dumps(response.json(), indent=4)
print(formatted)

# Optional – Print joke clearly (nice to include)
joke = response.json()
print("\n=== JOKE RESULT ===")
print(joke["setup"])
print("→ " + joke["punchline"])