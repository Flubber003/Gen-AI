age = int(input("How old are you? "))
if(age>=18):
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    i = 18-age
    print("Oops! You're not eligible yet. But hey, only " + str(i) +" more years to go!")
