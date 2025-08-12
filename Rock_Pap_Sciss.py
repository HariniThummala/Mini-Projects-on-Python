import random
print("********* Welcome to the Game *********")
print("        ROCK,PAPER and SCISSOR         ")
print("---------------------------------------")
print("R   Rock")
print("P   Paper")
print("S   Scissor")
ui=input("Enter Your Choice:")
if ui=='R':
   print(f"Your input is Rock")
elif ui=='P':
    print(f"Your input is Paper")
else:
    print(f"Your input is Scissor")
ci=random.choice('RPS')
if ci=='R':
   print(f"Computer input is Rock")
elif ci=='P':
    print(f"Computer input is Paper")
else:
    print(f"Computer input is Scissor")
if ui=='R' and ci=='S':
    print("You won!")
elif ui=='S' and ci=='R':
    print("Computer won!")
elif ui=='S'and ci=='P':
    print("You won!")
elif ui=='P'and ci=='S':
    print("Computer won!")
elif ui=='P'and ci=='R':
    print("You won!")
elif ui=='R'and ci=='P':
    print("Computer won!")
else:
    print("It is a tie!")
print("---------------------------------------")
