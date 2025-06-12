me = {"name": "Sterling", "age":"22", "city": "Kathleen"}
me["favorite color"] = "green"
me["city"] = "Atlanta"
print("Keys: ", end="")
for x in me:
    print(x + ", ", end="")
print()
print("Values: ", end= "")
for a in me:
    print(me[a] + ", ", end="")
