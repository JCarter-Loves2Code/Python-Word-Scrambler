import random

animals = [
    "lion", "tiger", "elephant", "giraffe", "zebra",
    "cheetah", "gorilla", "kangaroo", "panda", "wolf",
    "fox", "rabbit", "eagle", "penguin", "dolphin"
]

food = [
    "pizza", "burger", "pasta", "sushi", "tacos",
    "rice", "chicken", "steak", "lasagna", "pancakes",
    "fries", "sandwich", "curry", "salad", "ice cream"
]

countries = [
    "barbados", "canada", "brazil", "japan", "germany",
    "france", "mexico", "india", "australia", "spain",
    "italy", "china", "jamaica", "nigeria", "norway"
]


def play_game(category, words):
    random_word = random.choice(words)
    scrambled_word = ''.join(random.sample(random_word, len(random_word)))

    print(f"\n=== WELCOME TO THE {category.upper()} SCRAMBLER ===")
    print(f"The scrambled {category.lower()} word is: {scrambled_word}")

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = input(
            f"Please enter your guess [YOU HAVE {max_attempts - attempts} GUESSES]: "
        ).lower()

        attempts += 1

        if guess == random_word:
            print(
                f"\nCONGRATULATIONS! YOU GUESSED CORRECTLY."
                f"\nThe correct word was {random_word}"
            )
            return

        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"You guessed wrong. You have {remaining} guesses remaining.")
        else:
            print(
                f"\nYou ran out of attempts!"
                f"\nThe answer was {random_word}."
                f"\nBetter luck next time!"
            )


while True:
    print("\n=== WELCOME TO THE SCRAMBLER PROGRAM ===")
    print(
        "Which Category Would You Like To Play In:"
        "\n1. Food"
        "\n2. Country"
        "\n3. Animals"
        "\n4. Exit"
    )

    try:
        option = int(input("Please enter your choice: "))

        match option:
            case 1:
                play_game("Food", food)

            case 2:
                play_game("Country", countries)

            case 3:
                play_game("Animals", animals)

            case 4:
                print("\nSo sorry to see you go my friend.")
                print("Have a wonderful day!")
                break

            case _:
                print("Invalid option. Please choose 1, 2, 3, or 4.")

    except ValueError:
        print("Invalid input. Please enter a number.")
