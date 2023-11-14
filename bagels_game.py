#
# Bagels Game example
#
import random

num_digit = 3 # needs to be max 10 digit
max_guesses = 10

def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secret_num = ''
    for i in range(num_digit):
        secret_num += str(numbers[i])
        
    return secret_num

def get_clues(guess, secret_num):
    
    if guess == secret_num:
        return 'You got it!'

    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    print(f'''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {num_digit}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.''')
    
    while True:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {max_guesses} guesses to get it.')
        
        num_guesses = 1
        while num_guesses < max_guesses:
            guess = ''
            while len(guess) != num_digit or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input()
                
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1
            
            if guess == secret_num:
                break
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')
                
        print('Do you want to play again? (yes/no)')
        if not input().lower().startswith('y'):
            break
    print('Thanks for playing!')
        
if __name__ == '__main__':
    main()