import random

def get_computer_choice():
    """Randomly select Rock,Paper,or Scissors for the Computer. """
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice =="scissors")or \
         (user_choice == "scissors" and computer_choice =="paper")or \
         (user_choice == "paper" and computer_choice =="rock"):
        return "win"
    else:
        return "lose"

def display_results(user_choice,computer_choice,result):
    """Display the results of the game ."""  
    print(f"\nYou choose : {user_choice}") 
    print(f"The computer choose : {computer_choice}") 
    if result == "win":
        print("Congratulations ! You win !!!!!")
    elif result == "lose":
         print("Sorry, you lose. Better luck next time !!")
    else:
        print("It is a tie !!")

def main():
    user_score =0
    computer_score =0

    print("Let's Play Rock,Paper,Scissor!!")

    while True:
        user_choice = input("\nEnter your choice(rock ,paper,or scissors):").lower()
        if user_choice not in ["Rock","Paper","Scissor"]:
            print("Invalid choice.Please choose rock.paper.scissor.")
            continue
        computer_choice=get_computer_choice()
        result=determine_winner(user_choice,computer_choice)

        display_results(user_choice,computer_choice,result)

        if result == "win":
            user_score+=1
        elif result == "lose":
            computer_score +=1

        print(f"\nScore - You {user_choice} |Computer:{computer_choice}")

        play_again = input("\nDo you want to play again ? (yes/no):").lower()
        if play_again != "yes":
            print("Thanks for playing !!!")
            break 
            
if __name__ == "__main__":
    main()


