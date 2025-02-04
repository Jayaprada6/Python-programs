import random

rps=('r','p','s')
emojis={'r':'🪨','p':'📃','s':'✂️'}
while True:
    user_input=input("Rock,Paper or Scissor? (r/p/s): ").lower()

    if user_input not in rps:
        print("Invalid input, Please choose 'r','p' or 's'.")
        continue
    
    computer=random.choice(rps)

    print("Your choice ",emojis[user_input])
    print("Computer choice ",emojis[computer])

    if user_input==computer:
        print("It's a Tie☹️")
    elif (user_input=="r" and computer=="s") or (user_input=="p" and computer=="r") or (user_input=="s" and computer=="p"):
        print("You Win!!!🎉")
    else:
        print("You Lose😞")

    play_again=input("Want to play agian? (y/n): ").lower()
    if play_again!="y":
        print("Thanks for Playing👋")
        break