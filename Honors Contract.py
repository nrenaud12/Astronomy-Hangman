#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random


# In[16]:


def choose_word():
    words = ["astrophysics", "quantum", "astronomy", "black hole", "stars", "comet", "eclipse", "celestial", 
             "drawf planet", "terrestrial", "exoplanet", "gravity", "interstellar", "meteor", 
             "nebula", "aphelion", "perihelion", "telescope", "wormhole", "zenith", 
             "earth", "mars", "mercury", "venus", "saturn", "jupiter", "neptune", "pluto", "europa", 
             "pulsar", "quasar", "fermion", "boson", "neutron star", "cosmology", 
            ]
    
    return random.choice(words)


# In[17]:


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


# In[18]:


def display_hangman(incorrect_guesses):
    stages = [
        """
        -----
        |   |
            |
            |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\  |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\  |
       /    |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\  |
       / \  |
            |
        ------
        """
    ]
    return stages[incorrect_guesses]


# In[19]:


def hangman():
    print("Welcome to the Astronomy Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    while incorrect_guesses < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word:", current_display)
        print(display_hangman(incorrect_guesses))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter")

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            print("Incorrect guess. Attempts left:", max_attempts - incorrect_guesses - 1)
            incorrect_guesses += 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if incorrect_guesses == max_attempts:
        print(display_hangman(incorrect_guesses))
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)


# In[ ]:


hangman()

