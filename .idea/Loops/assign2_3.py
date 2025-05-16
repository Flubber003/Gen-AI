c = input("Please insert a whole number: ")
c = int(c)
result = 1
for i in range(1, c+1):
    result*= i
print("The factorial of "+str(c)+" is "+ str(result))
