from random import randrange

numbers= randrange(1,10)
print("Guess a number between 1-10")
userInput= 0
while numbers != userInput:
    userInput= int(input())
    if userInput > numbers:
        print("Too High")
    elif userInput < numbers:
        print("Too Low")
    elif userInput == numbers:
        print("Good Job!")
        break
