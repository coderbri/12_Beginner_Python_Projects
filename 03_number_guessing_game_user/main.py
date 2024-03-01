import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"\nGuess a number between 1 and {x}: "))
        # print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    print(f'Yay, congrats. You have guessed the number, {random_number}.')


def computer_guess(x):
    low = 1
    high = x
    won_legitimately = False
    
    feedback = ''
    while feedback != 'c':
        '''
        while feedback != 'c' and low != high:
        # ! this would not be good to use as we want the user to confirm if the computer guessed the number instead of the computer automating to determine the correct answer
        '''
        if low <= high:
            guess = random.randint(low, high)
        else:
            print("Invalid feedback sequence. Please provide consistent feedback.")
            break
        
        feedback = input(f'Is {guess} too high (H), to low (L), or correct (C)?? ').lower()
        if feedback == 'q':
            print("\nQuitting the game...")
            return
        
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter 'H' for too high, 'L' for too low, or 'C' for correct.\n")
    
    if feedback == 'c':
        won_legitimately = True
    if won_legitimately:
        print(f'Yay! The computer guessed your number, {guess}, correctly!')

# guess(10)
computer_guess(10)