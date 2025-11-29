

bot_age: int = 3

name = input("Hello! What is your name? ")
name_cap = name.capitalize()

print(f"Nice to meet you {name_cap}!")

age_input = input("How old are you? ")
age = int(age_input)
age_difference = age - bot_age

print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color? ")
color_cap = color.capitalize()

print(f"{name_cap}, {color_cap} is a beautiful color!")
