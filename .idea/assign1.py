name = "Trey"
age = 22
height = 5.0
print("Hey there, my name is "+ name +"! I'm "+ str(age) +" years old and "+ str(height) +" feet tall.")
num1 = 10
num2 = 3
print("The sum of 10 and 3 is", num1+num2)
print("The difference of 10 and 3 is", num1-num2)
print("The product of 10 and 3 is", num1*num2)
print("The quotient of 10 and 3 is", num1/num2)
print("Input a whole number here:")
a = input()
a = int(a)
if(a>0):
    print("This number is positive. Awesome!")
elif(a<0):
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
