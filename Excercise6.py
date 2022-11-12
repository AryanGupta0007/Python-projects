# Snake Water Gun
import random
print("Hi , Lets play a game \nThe Game is called Snake Water Gun "
"The rules of the game are quite simple \nYou have to make a choice out of Snake "
"Water or Gun and I will make a choice of  my own(The Computer) \nIf one choose Snake and other choose"
"Gun then Gun wins as Gun Kills the Snake\nSimilarly, If one chooses a Gun while the"
"other choose water then water will be the winner as water drowns Gun\nand lastly"
"If one choose snake and the other choose water then snake will win as snake drink"
" water\nand If we choose the same then it's a tie I hope the rules are pretty simple"
" and clear to you \nEven if you still have any doubt then "
"  you will learn while playing\nLet's Begin our 11 round series and one with"
"most wins will be declared winner")
rounds = 1
computer_points = 0
user_points = 0
while(rounds<12):
    available_choices = ["Snake","Water","Gun"]
    user_choice = input("To Choose Snake (press 1) , Water(press 2) , Gun(press 3)\n")
    computer_choice = random.choice(available_choices)

    while(user_choice.isnumeric() == False or int(user_choice) > 3):
        user_choice = input("Enter a valid Input . To Choose Snake (press 1) , Water(press 2) , Gun(press 3)\n")
        continue
    
# if i enter a string in this loop it shows error , how to ask user for input 
# when he enters string     


    if(computer_choice == "Snake" and int(user_choice) == 1):
        print("Oh it's a tie as we both chose Snake ")
    

    if(computer_choice == "Water" and int(user_choice) == 2):
        print("Oh it's a tie as we both chose Water ")
    
    if(computer_choice == "Gun" and int(user_choice) == 3):
        print("Oh it's a tie as we both chose Gun ")
        
    if (computer_choice == "Snake" and int(user_choice) == 2):
        print(f"You Lose as I chose {computer_choice} and Snake drinks Water")
        computer_points += 1 

    elif (computer_choice == "Gun" and int(user_choice) == 1):
        print(f"You Lose as I chose {computer_choice} and Gun kills Snake")
        computer_points += 1

    elif (computer_choice == "Water" and int(user_choice) == 3):
        print(f"You Lose as I chose {computer_choice} and Water drowns Guns")
        computer_points += 1


    elif (computer_choice == "Snake" and int(user_choice) == 3):
        print(f"You Won as I chose {computer_choice} and Gun kills Snake")
        user_points += 1
    elif (computer_choice == "Water" and int(user_choice) == 1):
        print(f"You Won as I chose {computer_choice} and Snake drinks Water")
        user_points += 1
    elif (computer_choice == "Gun" and int(user_choice) == 2):
        print(f"You Won as I chose {computer_choice} and Water drowns Guns")
        user_points += 1
    rounds += 1    

print(f"Game Over the final scores after 11 rounds are \n{computer_points}"
f" - Computer\n{user_points} - Your Points")
if(computer_points > user_points):
    print("Computer Won")

if(computer_points < user_points):
    print("You Won")

if(computer_points == user_points):
    print("Tie")
input("press Enter to exit")