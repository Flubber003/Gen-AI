password = str(input("Enter a password: "))
special = "!@#$%^&*()-+?_=,<>/"
spcount = 0
digcount = 0
uppcount = 0
count = 0
for char in password:
    count+=1
    if char in special:
        spcount+=1
    if char.isdigit():
        digcount+=1
    if char.isupper():
        uppcount+=1
strength = 100
if(count>=8 and spcount>=1 and digcount>=1 and uppcount>=1):
    print("Your password is strong.")
    print("Your password strength is 10/10")
else:
    flag = []      #I don't think I'm allowed to use lists, but this was the only way to keep me from writing 16 different outcomes.
    if(spcount < 1):
        flag.append("a special character")
        strength -= 25
    if(digcount < 1):
        flag.append("a digit")
        strength -= 25
    if(uppcount < 1):
        flag.append("an uppercase letter")
        strength -= 25
    if(count < 8):
        flag.append("at least 8 characters")
        strength -= 25
    print("Your password needs " + ", ".join(flag) + ".")
    print("Your password strength is " + str(int(strength/10)) + "/10")
