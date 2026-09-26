import random

animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Zebra",
    "Cheetah", "Gorilla", "Kangaroo", "Panda", "Wolf",
    "Fox", "Rabbit", "Eagle", "Penguin", "Dolphin"
]

food = [
    "Pizza", "Burger", "Pasta", "Sushi", "Tacos",
    "Rice", "Chicken", "Steak", "Lasagna", "Pancakes",
    "Fries", "Sandwich", "Curry", "Salad", "Ice Cream"
]

countries = [
    "Barbados", "Canada", "Brazil", "Japan", "Germany",
    "France", "Mexico", "India", "Australia", "Spain",
    "Italy", "China", "Jamaica", "Nigeria", "Norway"
]

while True:

    print("\nWELCOME TO THE SCRAMBLER GAME")
    print("Please select which category you would like to play:")
    print("1. Animals")
    print("2. Food")
    print("3. Countries")

    choice = int(input("Choice?: "))

    match choice:

        case 1:
            randomAnimal = random.choice(animals)
            scrambledAnimal = ''.join(
                random.sample(randomAnimal, len(randomAnimal))
            )

            print(f"\nUnscramble this animal: {scrambledAnimal}")
            print("YOU HAVE 5 GUESSES")

            attempts = 0
            userGuess = input("What is your guess?: ")
            attempts += 1

            while userGuess != randomAnimal and attempts < 5:
                userGuess = input("Wrong guess, try again: ")
                attempts += 1

            if userGuess == randomAnimal:
                print(f"CONGRATULATIONS! The correct word was {randomAnimal}")
            else:
                print(f"Out of guesses! The correct word was {randomAnimal}")

        case 2:
            randomFood = random.choice(food)
            scrambledFood = ''.join(
                random.sample(randomFood, len(randomFood))
            )

            print(f"\nUnscramble this food: {scrambledFood}")
            print("YOU HAVE 5 GUESSES")

            attempts = 0
            userGuess = input("What is your guess?: ")
            attempts += 1

            while userGuess != randomFood and attempts < 5:
                userGuess = input("Wrong guess, try again: ")
                attempts += 1

            if userGuess == randomFood:
                print(f"CONGRATULATIONS! The correct word was {randomFood}")
            else:
                print(f"Out of guesses! The correct word was {randomFood}")

        case 3:
            randomCountry = random.choice(countries)
            scrambledCountry = ''.join(
                random.sample(randomCountry, len(randomCountry))
            )

            print(f"\nUnscramble this country: {scrambledCountry}")
            print("YOU HAVE 5 GUESSES")

            attempts = 0
            userGuess = input("What is your guess?: ")
            attempts += 1

            while userGuess != randomCountry and attempts < 5:
                userGuess = input("Wrong guess, try again: ")
                attempts += 1

            if userGuess == randomCountry:
                print(f"CONGRATULATIONS! The correct word was {randomCountry}")
            else:
                print(f"Out of guesses! The correct word was {randomCountry}")

        case _:
            print("Invalid choice.")
