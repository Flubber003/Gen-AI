list = ['one', 'two', 'three']
me = {"name": "Sterling", "age":"22", "city": "Kathleen"}
try:
    print(list[3])
except IndexError:                              # list[3] is out of range. Python raises an error which is caught by the except block and prints the custom message.
    print("IndexError occurred! List index out of range.")

try:
    print(me["blank"])
except KeyError:                                # Dictionary contains no "blank key". Python raises an error which is caught by the except block and prints the custom message.
    print("KeyError occurred! Key not found in the dictionary.")

try:
    print(list[2]+1)
except TypeError:                               # Can't add string 'three' to an interger. Python raises an error which is caught by the except block and prints the custom message.
    print("TypeError occurred! Unsupported operand types.")