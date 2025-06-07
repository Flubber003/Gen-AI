base = str(input("Enter a word: "))
base1 = base[::-1]
if(base == base1):
    print("Yes, '" + base + "' is a palindrome!")
else:
    print(base + " is not a palindrome.")