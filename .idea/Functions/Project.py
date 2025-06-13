import turtle
def factorial(n):                                   #Factorial function
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):                                    #Fibonacci function
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
def draw_tree(branch_length,t):                       #Drawing function - try not to go above 100 branch length
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)
ans = 0
print("Welcome to the Recursive Artistry Program! Choose an option: ")

while ans != 4:
    print("\n1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Draw a recursive fracal pattern.")
    print("4. Exit")
    ans = input()
    ans = int(ans)
    if ans == 1:
        print("Enter a number: ")
        val = input()
        val = int(val)
        print("The factorial of",val,"is", str(factorial(val)))
    elif ans == 2:
        print("Enter a number: ")
        val = input()
        val = int(val)
        print("The", val,"\bth Fibonacci number is", str(fibonacci(val)))
    elif ans == 3:
        print("Enter a number for the branch length: ")
        val = input()
        val = int(val)
        if val > 100:
            print("Too long! Capping to 100.")
            val = 100
        screen = turtle.Screen()
        screen.title("Simple Fractal Tree 🌳")
        t = turtle.Turtle()
        t.left(90)           # Point turtle upwards
        t.up()
        t.backward(100)      # Move back to give space for drawing
        t.down()
        t.color("green")
        t.speed(0)
        draw_tree(val,t)
        screen.mainloop()
    elif ans == 4:
        print("Gooodbye!")
        break
    else:
        print("Enter a number between 1 and 4.")