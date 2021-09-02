from game_data import data
import random
import art
from replit import clear


comparison = random.choice(data)
cFollower = comparison["follower_count"]
against = random.choice(data)
aFollower = against["follower_count"]
if comparison == against:
    against = random.choice(data)

score = 0

play_game = True
while play_game:
    clear()
    print(art.logo)
    if score > 0 and play_game:
        print(f"You're right! Current score: {score}.")
    print(f'Compare A: {comparison["name"]}, a {comparison["description"]}, from {comparison["country"]}.{comparison["follower_count"]}')
    print(art.vs)
    print(f'Against B: {against["name"]}, a {against["description"]}, from {against["country"]}.{against["follower_count"]}')
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    

    if cFollower > aFollower and guess == "a":
        score += 1
        comparison = against
        cFollower = comparison["follower_count"]
        against = random.choice(data)
        if comparison == against:
            against = random.choice(data)
        aFollower = against["follower_count"]
    elif cFollower < aFollower and guess == "b":
        score += 1
        comparison = against
        cFollower = comparison["follower_count"]
        against = random.choice(data)
        if comparison == against:
            against = random.choice(data)
        aFollower = against["follower_count"]
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
    
    