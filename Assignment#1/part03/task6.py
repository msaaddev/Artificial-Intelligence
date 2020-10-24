"""
	Name: Muhammad Saad
	Reg#: 2018-CS-7
"""

user1Choice = input(
    "What do you want to choose player #1?(rock, paper or scissors) ")
user2Choice = input(
    "What do you want to choose player #2?(rock, paper or scissors) ")


def rockPaperScissor(firstUser, secondUser):
    if firstUser == secondUser:
        return("It's a tie!")
    elif firstUser == 'rock':
        if secondUser == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif firstUser == 'scissors':
        if secondUser == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif firstUser == 'paper':
        if secondUser == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")


print(rockPaperScissor(user1Choice, user2Choice))
