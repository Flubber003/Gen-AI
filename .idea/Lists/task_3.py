fav_art = ('Captian America', 'Pray for Paris', 'Blackest Night' )
try:
    fav_art[0] = "The Matrix"
except TypeError as e:
    print("Error:", e)
print("Length of tuple:", len(fav_art) )