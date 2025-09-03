words = {"eye" : 3, "fair" : 4, "pencil" : 5}


def main ():
    print("Welcome to spelling bee game :)")
    print(" Your given letters are: L R E I V N P A F Y")
    


    while len(words) > 0:
        print (f"{len(words)} words are left")
        guess = input("Guess a word: ").strip().lower()

        if guess in words.keys():
            points = words.pop(guess)
            print(f"Good job! You scored {points} points")
            

        else:
            print ("Incorrect!")

    
    print ("Thats all the the words! Game over")


main ()