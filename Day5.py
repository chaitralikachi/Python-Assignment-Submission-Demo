import random

name=input("Enter your name -\n")
print("Good luck!",name)

words=['string','row','tupple','mutable','immutable','class','object','list']

word=random.choice(words)

print("Guess the characters ")

guesses=''

turns = 12

while turns > 0 :
    failed = 0

    for char in word :
        if char in guesses :
            print(char)

        else:
            print("_")

            failed+=1

    if failed==0:
        print("You win :)")

        print("The word is - ",word)
        break

    guess=input("Guess a character :")
    guesses+=guess

    if guess not in word:
        turns-=1

        print("wrong, guess again")

        print("You have ",+ turns ,"more guesses")

        if turns==0:
            print("Game over :(")
