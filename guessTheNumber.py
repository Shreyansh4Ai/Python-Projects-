import random 


def guess (x):
    random_num = random.randint(1,x)
    guess=0
    while guess!= random_num :
        user_input = input(f'Guess a number between 1 and {x}: ')
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(user_input)
        if guess < random_num:
            print("Guess again, too low. ")
        elif guess > random_num:
            print("Guess again, too high")    

    print(f"Congrats! You got it. {random_num} is the answer.")


guess(10)