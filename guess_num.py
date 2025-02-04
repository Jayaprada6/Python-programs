import random 

num=random.randint(1,100)
print(num)
while True:
    try:
        guess=int(input("Guess the number between 1 to 100: "))
    except ValueError:
        print("Please enter the valid number")
        continue

    if(guess<num):
        print("Too Low!")
    elif(guess>num):
        print("Too High!")
    else:
        print("Congratulations! you guessed the number.")
        break
    
   


        