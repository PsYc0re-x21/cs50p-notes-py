words = {"eye" : 3, "fair" : 4, "pencil" : 5}


def main ():
    print("Welcome to spelling bee game :)")
    for word, points in words.items():
        print(f"{word} was worth of {points} points")

main()