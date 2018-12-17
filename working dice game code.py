import random
diceroll = random.randint (1,5)
count = 0
pointsForMatching = 0

userName = input("Enter your name please:")

print(userName,"Welcome if you guess the number once you have won")

# Loop to repeat the game
while count < 3:

# UserGuess
    count = count + 1


    userGuess = eval(input("Guess the number (1,5): "))


# if condition
    if userGuess == diceroll:
     print("Congrats You Guess It Correct !!\n You have Won")
     pointsForMatching = pointsForMatching + 1
     print("Point:", pointsForMatching)
     count = 5

    else:
        print("Sorry try again, you have :", 3- count , "Chance left")


    

print("Game over")   
print("Thank you for playing my game")

# outcome of the game 
# you either win or lose
