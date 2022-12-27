print("Rules of the game:-")
print("You have to choose a number from 1 to 6, if your input and input of the diceroll is same then you will be rewarded by (+10)")
print("If your input and input of the diceroll is not same then you will be rewarded by (-1)")
print("This will continue untill you stop the game")
import random
e=input("Do you wish to continue (Y/y for Yes) or (N/n for no): ")
g="Yy"
points=0
l1=['Y','y','N','n']
if e not in l1:
    print("Please type the right input (Y/y for Yes) or (N/n for no)")
while e in  g:
    print("Your current points are {}".format(points))
    print("Enter your number of choice between 1 to 6")
    a=int(input("Enter your choice: "))
    c=random.randint(1,6)
    if a==c:
        points=points+10
        print("The diceroll gave the number {}".format(c))
        print("You win")
        print("Your current points are: {}".format(points))
    elif a>6 or a<1:
        print("Invalid input, Enter number between 1 to 6!")
    else:
        points=points-1
        print("The diceroll gave the number {}".format(c))
        print("Since the dice rolled number and your choice are not same")
        print("You lose")
        print("Your current points are: {}".format(points))
    e=input("Do you wish to continue (Y/y for Yes) or (N/n for no): ")
else:
    print("Thank you for playing")
    print("Hope you enjoyed!:)")

    