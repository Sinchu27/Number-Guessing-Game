#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user input for the guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

# Run the game
number_guessing_game()


# ### 
