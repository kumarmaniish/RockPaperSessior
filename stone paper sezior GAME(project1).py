import random
print("\t\t__stone__paper__scissor__")
print("\t\t\t___GAME___\n\n")
a=["stone","paper","scissor"]
count=0
win=0
draw=0
lose=0
while count<7:
    computer=random.choice(a)
    you=input("Choose stone/paper/scissor ---->  ")
    if computer==you:
        print()
        print("Computer choice >>>------>>",computer)
        print(" both are choosen the same means >>---->> Match Draw")
        print()
        draw=draw+1
    else:
        if computer=="stone":
            if you=="paper":
                print()
                print("computer choice >>-->",computer)
                print("you win the game")
                print()
                win=win+1
            if you=="scissor":
                print()
                print("Computer choice >>--->",computer)
                print("you lost the game")
                print()
                lose=lose+1
        elif computer=="paper":
            if you=="stone":
                print()
                print("Computer choice >>-->",computer)
                print("you lost the game")
                print()
                lose=lose+1
            if you=="scissor":
                print()
                print("Computer choice >>--->",computer)
                print("you win the game")
                print()
                win=win+1
        elif computer=="scissor":
            if you=="stone":
                print()
                print("Computer choice >>--->",computer)
                print("you win the game")
                print()
                win=win+1
            if you=="paper":
                print()
                print("Computer choice >>--->",computer)
                print("you lost the game")
                print()
                lose=lose+1
        else:
            print()
    count=count+1
print()
print()
print()
print("\t\t\t___SUMMARY___")
print()
print("\t\t____Thats__your__results____")
print()
print("\tYOU WIN >>----> ",win)
print()
print("\tCOMPUTER WIN >>----> ",lose)
print()
print("\tMATCHES WHICH ARE DRAWS >>------> ",draw)
print()
print()
print()
print()
z=input()
