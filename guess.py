import random 
print("Number guessing game")
number=random.randint(1,9)
chance=0
print("guess a number between 1-9:")
while chance<5:
    guess=int(input("enter your guess:"))
    if guess==number:
        print("Congrats")
        break 
    elif guess<number:
        print("guess a higher number")
    else:
        print("guess a lower number")
    chance+=1
if not chance<5:
    print("you loose!the number is ",number)