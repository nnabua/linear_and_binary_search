import random

# Guess a number


def guess_random_number(tries, start, stop):

    random_num = random.randint(start, stop)
    print(random_num)
    while tries != 0:
        print(f"Number of tries left {tries}")
        guess_number = int(
            input(f"Guess a number between {start} and {stop}: "))
        if guess_number == random_num:
            return print("You guessed the correct number!")
        elif random_num > guess_number:
            print("Guess highers!")
            tries -= 1
        elif random_num < guess_number:
            print("Guess lower!")
            tries -= 1
        if tries == 0:
            print(f"You have failed to guess the number {random_num}")


""" Task 1: Driver Code"""
guess_random_number(5, 0, 10)


# Guess a number using linear search
def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f"\nThe number for the program to guess is: {random_num}")
    guess_num = range(start, stop)
    for num in guess_num:
        num = random.choice(guess_num)
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing: {num}")
        if num is random_num:
            return print("The program has guessed the correct number! ")
        else:
            tries -= 1
        if tries == 0:
            return print("The program has failed to guess the number.")


""" Task 2: Driver Code"""
guess_random_num_linear(5, 0, 10)


# Finding number using binary search
def guess_random_num_binary(tries, start, stop):

    random_num = random.randint(start, stop)
    print(f"\nRandom number to find: {random_num}")

    lower_bound = start
    upper_bound = stop

    while tries != 0 and lower_bound <= upper_bound:

        computer_guess = random.randint(lower_bound, upper_bound)
        pivot = (lower_bound + upper_bound) // 2

        if computer_guess == random_num:
            print(f"Found it! {random_num}")
            break

        elif random_num > pivot:
            lower_bound = pivot + 1
            pivot = (lower_bound + upper_bound) // 2
            tries -= 1
            print("Guessing higher!")

        elif random_num < pivot:
            upper_bound = pivot - 1
            pivot = (lower_bound + upper_bound) // 2
            tries -= 1
            print("Guessing lower")

        if tries == 0:
            print("Program failed to find the number")
            break


""" Task 3: Driver Code"""
guess_random_num_binary(5, 0, 100)
