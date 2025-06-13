def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:", end="")
    for item in args:
        print(f" - {item}", end="")


ingredients = [
    "Bread",
    "Turkey",
    "Ham",
    "Cheese",
    "Lettuce",
    "Tomato",
    "Mayonnaise",
    "Mustard",
    "Pickles"
]


make_sandwich(*ingredients)