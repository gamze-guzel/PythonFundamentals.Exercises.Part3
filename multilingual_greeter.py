def greet(name):
    print("Hello " +name)

def name_input():
    print("What's your name?")
    name=input()
    return name

def language_input():
    print("1.Turkish, 2.English, 3.Spanish")
    userInput = int(input())
    if userInput == 1:
        print("Merhaba " + name_input())
    elif userInput == 2:
        print("Hello " + name_input())
    elif userInput == 3:
        print("Hola " + name_input())

language_input()