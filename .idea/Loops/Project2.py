import random
num = random.randint(1,100)
a = -1
count = 0
while(a!=num):
    print("Guess the number (between 1 and 100): ", end=" ")
    a = input()
    a = int(a)
    count+=1
    if(a==num):
        print("Congratulations! You guessed it in "+ str(count) +" attempts!")
    if(a>num and count!=10):
        print(str(a) + " Too high! Try again.")
    if(a>num and count==10):
        print(str(a) + " Too high!")
    if(a<num and count!=10):
        print(str(a) + " Too low! Try again.")
    if(a<num and count==10):
        print(str(a) + " Too low!")
    if(count==10):
        print("Game Over! Better luck next time!")
        break