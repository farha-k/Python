# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 17:48:01 2025

@author: saofl
"""
import random
words=["apple","banana","cherry","mango","kiwi","pinapple","lichi","orange"]
word=random.choice(words)
guessed_word=["_"]*len(word)
wrong_attempts=6
guessed_letters=[]
print("WELCOME TO HANGMAN GAME")
print("\nHow to Play:")
print("1. I will choose a secret word.")
print("2. You will try to guess it, one letter at a time.")
print("3. If your guess is correct, the letter will be revealed.")
print("4. If it's wrong, a part of the hangman is drawn.")
print("5. You lose if the whole hangman is drawn before guessing the word.")
print("\nTips:")
print("- Only enter one letter at a time.")
print("- Avoid repeating letters you've already guessed.")
print("- Think before you guess — too many wrong guesses and you're done!\n")
print(f"You have {wrong_attempts} attempts.")
print("Let's start!\n")
while wrong_attempts>0:
    guess=input("Guess a letter:").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Good guess")
        for i in range(0,len(word)):
            if word[i]==guess:
                guessed_word[i]=guess
    else:
        print("Wrong guess")
    wrong_attempts-=1
    print("".join(guessed_word))
    print("Attempts left:",wrong_attempts)
if "_" not in guessed_word:
    print("Congratulations!You guessed the word:",word)
else:
    print("Game over!The word was:",word)