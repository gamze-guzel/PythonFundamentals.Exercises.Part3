from random import randrange
print(randrange(10))


numbers= randrange(1,10)
print("Guess a number between 0-10")
input= 0
while numbers != input:
    input= int (numbers())
    if input > numbers:
        print ("Too High")
    elif input < numbers:
        print ("Too Low")
    elif input == numbers:
        print("Game Over")
        break
