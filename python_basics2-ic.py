def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #challenge()



#PROBLEM1
#Create a function that has two variables.
# One called greeting and another called myName.
# Print out greeting and myName two different ways without using the following examples
def problem1():
    greeting = "Hello"
    myName = "Didi"

    print(f"{greeting},{myName}")
###########################################################################################################
#PROBLEM2
#Create a function that asks the user for a secret password.
# Create a loop that quits with the user's quit word.
# If the user doesn't enter that word, ask them to guess again.
def problem2():
    userInput = input("Enter a secret password: ")
    userInput2 = " "
    while(userInput != "q"):
        if (userInput != userInput2):
            userInput2 = input("Please enter the correct one:  ")
        else:
            print("CORRECT")
            break
###########################################################################################################
#PROBLEM3
#Create a function that prints 0 to 100 three times in a row (vertically).
def problem3():
    for num1 in range(3):
        for num in range(101):
            print(num)
###########################################################################################################
#PROBLEM4
#Create a random number.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
def problem4():
    userInput = int(input("Guess a random number: "))
    import random
    randomNum = random.randint(0,9)
    print(randomNum)
    while(userInput != randomNum):
        if(True):
            userInput = int(input("Guess a random number: "))
        else:
            print("")
###########################################################################################################
#CHALLENGE
#Ask the user to create a number for the computer to guess.
# Create random numbers until the computer gets that number.
# Once it guesses the number, alert the user how many times it took to guess the random number.
def challenge():
    userInput = int(input("create a number for the computer to guess: "))
    countsForComputer = 0
    computerGuess = random.randint(0,1000)

    while(computerGuess != userInput):
        countsForComputer+=1
        computerGuess = random.randint(0,1000)
    print(f"it's took the computer {countsForComputer}many times to guess.")







###########################################################################################################
if __name__ == '__main__':
    main()