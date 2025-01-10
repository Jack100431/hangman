import random
import copy

name = str(input("Hello! Please enter your name: "))
print(f"Hello, {name}! Welcome to the game!")
print("Now there's a poor guy that need your rescue. Please help him!")

def hangman(time):
    if time == 5:
        print("  o  ")
    if time == 4:
        print("  o  ")
        print("  |  ")
    if time == 3:
        print('  o  ')
        print(' /|  ')
    if time == 2:
        print('  o  ')
        print(' /|\\  ')
    if time == 1:
        print('  o  ')
        print(' /|\\  ')
        print(' /   ')
    if time == 0:
        print('  o  ')
        print(' /|\\  ')
        print(' / \\')

def gamemode(words, round_time, try_time):
    word = str(random.choice(words)) #The system will randomly pick a word for the user to guess.
    words = [w for w in words if w != word]
    word1 = list(word)
    user = len(word) * "_ "
    user = user.strip().split(" ")
    print(user)
    print()
    print(f'There are total {len(word)} letter(s) in this word.')
    user1 = copy.copy(user)

    while try_time != 0 and user != word1:
        input_item = input("Please enter a letter or if you are certain, enter your answer: ").lower()
        while not input_item.isalpha:
            input_item = input("Please enter a letter or if you are certain, enter your answer: ").lower()
        if len(input_item) != 1:
            if input_item == word:
                user = word1
            else:
                try_time -= 1
                print(f"Your answer is incorrect. You have {try_time} time(s) left!")
                print()
                hangman(try_time)
                print()
                print(user)
        else:
            for i in range(len(word1)):
                if word1[i] == input_item:
                    user[i] = input_item
            if user1 == user:
                try_time -= 1
            else:
                user1 = copy.copy(user)
            print(user)
            print(f"You still have {try_time} time(s) left.")
            print()
            hangman(try_time)
            print()
            print(user)
    if user == word1:
        print(f"Congratulations! You made it! You still have {try_time} time(s) left!")
        try_time += 1
    else:
        print(f"Sorry, you lose in round {round_time}. The correct answer is {word}.")
    return user, word1, word, try_time, round_time, words
            
words = ["execute", "heita", "dilireba", "wonderful"] #Creating a word bank.
round_time = 1
try_time = 6
user, word1, word, try_time, round_time, words = gamemode(words, round_time, try_time)
if try_time > 0:
    decision = input("Do you want to start the next round?(Yes/No) ")
    decision = decision.lower()
    while decision == "yes" and round_time < 5:
        round_time += 1
        print(f"Round {round_time}")
        user, word1, word, try_time, round_time, words = gamemode(words, round_time, try_time)
        if round_time < 5:
            decision = str(input("Do you want to start the next round?(Yes/No) "))
            decision.lower()
if round_time == 5:
    round_time -= 1
print(f"Your totally complete {round_time} round(s).")