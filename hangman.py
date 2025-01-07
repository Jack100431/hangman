import random
import copy
words = ["python", "code", "student", "amazing"]
word = str(random.choice(words))
word1 = list(word)
user = len(word) * "_ "
user = user.strip().split(" ")
print(user)
print()
print(f'There are total {len(word)} letter(s) in this word.')
try_time = 6
user1 = copy.copy(user)

while try_time != 0 and user != word1:
    input_item = input("Please enter a letter: ").lower()
    while not input_item.isalpha():
        input_item = input("Please enter a letter: ")
    for i in range(len(word1)):
        if word1[i] == input_item:
            user[i] = input_item
    if user1 == user:
        try_time -= 1
    else:
        user1 = copy.copy(user)
    print(user)
    print(f"You still have {try_time} time(s) left.")
    decision = str(input("If you already have an answer, please type it. Otherwise please enter 'No'. You must understand that if your answer is incorrect, you will lose one chance for guessing. "))
    decision.lower()
    if decision != "no":
        if decision == word:
            user = word1
        else:
            try_time -= 1
if user == word1:
    print(f"Congratulations! You made it! You still have {try_time} time(s) left!")
else:
    print(f"Sorry, you lose. The correct answer is {word}.")