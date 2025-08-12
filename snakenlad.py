import random
l={5:15,9:19}
s={8:2,17:4,20:11}
ch=input("Do you want to play Snake & Ladder [y|n]: ")
if ch=='y':
    cur=0
    while(cur<25):
        n=random.randint(1,6)
        print("Dice number:",n)
        cur+=n
        if cur==5:
            cur=l[5]
        elif cur==9:
            cur=l[9]
        elif cur==8:
            cur=s[8]
        elif cur==20:
            cur=s[20]
        elif cur==17:
            cur=s[17]
        if cur>25:
            cur-=n
            print("Roll the Dice Again!")
        else:
            print("You are on:",cur)
    else:
        if cur==25:
            print("You Won!!!")
