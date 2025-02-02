import random
reply=input("Roll the dice?(yes/no) ")
reply_low=reply.lower()
if reply_low in ('yes'or'y'):
    dice_num=[1,2,3,4,5,6]
    ans=random.choices(dice_num,k=2)
    print(*ans,sep=",")
elif reply_low in ('no'or'n'):
    print("Thanks for Playing")
else:
    print("Invalid Choice, give 'yes or no'")