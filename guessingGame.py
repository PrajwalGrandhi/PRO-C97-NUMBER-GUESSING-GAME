import random

num=random.randint(0,9)

i=0
while i<=5:
    guess=int(input("Enter you guess: "))
    if guess==num:
        print("Congratulations!!!")
        break
    elif guess< num:
        print("too low a bit higher")
    else:
        print("too high a bit lower")
    i=i+1
    if(i==5):
        print("OUT OF CHANCES you lose, the number is",num)
        break