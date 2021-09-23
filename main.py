import random
rand_range = random.randrange(1, 4)

computers_move = ""

# Rock
if rand_range == 1:
    computers_move = "Rock"
# Paper
if rand_range == 2:
    computers_move = "Paper"
# Scissors
if rand_range == 3:
    computers_move = "Scissors"

humans_move = int(input("Rock (1) , Paper (2) , or Scissors (3) ?: "))

# User chooses Rock
if humans_move == 1:
    if computers_move == "Rock":
        print(f"You both chose {computers_move}")
    elif computers_move == "Paper":
        print(f"You Lost! The Computer Chose {computers_move}")
    else:
        print(f"You won! The computer chose {computers_move}")

# User chooses Paper
if humans_move == 2:
    if computers_move == "Paper":
        print(f"You both chose {computers_move}")
    elif computers_move == "Scissors":
        print(f"You Lost! The Computer Chose {computers_move}")
    else:
        print(f"You won! The computer chose {computers_move}")

# User chooses Scissors
if humans_move == 3:
    if computers_move == "Scissors":
        print(f"You both chose {computers_move}")
    elif computers_move == "Rock":
        print(f"You Lost! The Computer Chose {computers_move}")
    else:
        print(f"You won! The computer chose {computers_move}")