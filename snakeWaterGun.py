import random

def snakeWaterGun():
    choice_list = ["snake", "water", "gun"]

    try:
        user_choice = int(input("Choose between snake, water, and gun: 0:snake 1:water 2:gun: "))

        if user_choice not in [0, 1, 2]:
            print("Invalid choice. Please enter 0, 1, or 2.")
            return snakeWaterGun()  # retry

        computer_choice = random.choice(choice_list)
        print("user choice:", choice_list[user_choice])
        print("computer choice:", computer_choice)

        if choice_list[user_choice] == computer_choice:
            print("The match is draw")

        elif (choice_list[user_choice] == "snake" and computer_choice == "water") or \
             (choice_list[user_choice] == "water" and computer_choice == "gun") or \
             (choice_list[user_choice] == "gun" and computer_choice == "snake"):
            print("You won") 
        else:
            print("You lost")

    except Exception as e:
        print("Problem:", e)
        snakeWaterGun()  # retry on error

snakeWaterGun()
