
import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move=Rock, Paper,Scissor=")
comp_choice=random.choice(item_list)

print(f'user choice={user_choice}')
print(f'computer choice={comp_choice}')

if user_choice==comp_choice:
    print("both chooses same match tie")
elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("computer wins")
    else:
        print("rock smashes scissor =you win")
elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("scissor cuts paper ,computr win")
    else:
        print("paper covers rock,you win")
elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("paper cuts paper,you win")
    else:
        print("rock smashes scissor,computer win")
        
    
    