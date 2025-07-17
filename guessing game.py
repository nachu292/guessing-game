import os

# Keep asking until a valid single-digit number is entered
while True:
    real = input("enter a one-digit number: ")
    if not (real.isdigit() and len(real) == 1):
        print("please enter a valid one-digit number")
    else:
        os.system('cls')  # Clear the console on Windows
        break  # Exit the loop when a valid number is entered

# Guessing loop
while True:
    number = input("guess the number: ")
    if number == real:
        print("you won")
        break
    else:
        if int(number) > int(real):
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
