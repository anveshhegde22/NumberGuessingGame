import random
n=random.randint(1,100)
count=1
guess_chances=10
while 1<=guess_chances:
    num=int(eval(input("Guess the Number:")))
    if num>n:
        print("Your Guess was too High: Guess a number lower than",num)
    elif num<n:
        print("Your Guess was too low: Guess a number higher than", num)
    else:
        print("YOU WIN!")
        print(count,"Guesses You Took")
        break
    guess_chances-=1
    print((guess_chances,"Guesses Left"))
    count +=1
    print()
print("GAME OVER")
print("The Number is",n)
