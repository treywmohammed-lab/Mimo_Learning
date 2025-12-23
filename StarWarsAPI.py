#Customize

import requests

url = "https://swapi.mimo.dev/api/people"
number = 1
response = requests.get(url)

response.raise_for_status()
data = response.json()
print(f"There are {len(data)} entries")

if data:
    for entry in data:
        
        print(f"{number}. {entry["name"]}")
        number += 1
else:
    print("Sorry, there are not entries")

print()


# Project 
import requests

option = input("What StarWars data would you like to explore? ").strip().lower()

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Successfully fetched {len(data)} entities")
  except requests.HTTPError as e:
    print(f"Error fetching data: {e}")
    return None

  return data

data = fetch_data(option)

if data:
  for entity in data:
    print(entity["name"])
else:
    print("Unable to download data")
