from os import remove
from art import logo, vs
from game_data import data
import random

print(logo)

def show_data(pick):
    name = pick["name"]
    description = pick["description"]
    country = pick["country"]
    return f"Compare A: {name}, a {description}, from {country}"

def count_followers(picked):
    followers = int(picked["follower_count"])
    return followers

a_pick = random.choice(data)
b_pick = random.choice(data)
a = show_data(a_pick)
b = show_data(b_pick)
a_count = count_followers(a_pick)
b_count = count_followers(b_pick)
score = 0

print(a)
print(vs)
print(b)

picked = input("Who has more followers? Type 'A' or 'B': ").lower()

if picked == 'a':
    if a_count > b_count:
        score +=1
        remove()
    else:
        print(f"Sorry, that's wrong. final score: {score}")
        remove()
elif picked =='b':
    if a_count > b_count:
        print(f"Sorry, that's wrong. final score: {score}")
    else:
        score +=1


