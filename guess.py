import random

def guess():
    x = 10  # Define the range here, you can change 10 to any other number
    random_guess = random.randint(1, x)
    guess = 0
    
    while guess != random_guess:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_guess:
            print("Too low!")
        elif guess > random_guess:
            print("Too high!")
        else:
            print(f"Yay, congrats. You have gussed the num=number {random_guess} correctly!")
  


guess()
