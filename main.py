from game_data import data
import random
import art
from replit import clear

def format_data(account):
    """Format the account data in printable form"""
    accountName = account["name"]
    accountDesc = account["description"]
    accountCountry = account["country"]

    return f'{accountName}, a {accountDesc}, from {accountCountry}.'


def check_answer(guess, cFollower, aFollower):
    """Use if statement to check if user is correct and returns is they got it right"""
    if cFollower > aFollower:
        return guess == "a"
    else:
        return guess == "b"
    
print(art.logo)
score = 0
continueGame = True
against = random.choice(data)

while continueGame:

    comparison = against
    against = random.choice(data)
    while comparison == against:
        against = random.choice(data)


        
    print(f"Compare A: {format_data(comparison)}")
    print(art.vs)
    print(f"Against B: {format_data(against)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    cFollower = comparison["follower_count"]
    aFollower = against["follower_count"]

    is_correct = check_answer(guess, cFollower, aFollower)
    
    clear()
    print(art.logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continueGame = False
        print(f"Sorry, that's wrong. Final score: {score}")

    