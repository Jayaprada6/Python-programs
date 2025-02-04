import random
while True:
    reply=input("Roll the dice?(yes/no) ").lower()
    if reply in ('yes'or'y'):
        dice_num=[1,2,3,4,5,6]
        ans=random.choices(dice_num,k=2)
        print(*ans,sep=",")
    elif reply in ('no'or'n'):
        print("Thanks for Playing")
        break
    else:
        print("Invalid Choice, give 'yes or no'")
