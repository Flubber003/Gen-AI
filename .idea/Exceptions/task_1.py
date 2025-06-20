try:
    num = int(input("Enter a number: "))
    print("100 divided by 4 is", 100/num)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("You can't divide by zero.")