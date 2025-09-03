def recommend(game):
    print("You might like: \n", game)

def main():
    difficulty = input("Casual or Pro? : ").strip().title()
    if not (difficulty == "Casual" or difficulty == "Pro"):
        print("Enter a valid difficulty option")
        return

    players = input("Single or Multi?: ").strip().title()
    if not (players == "Single" or players == "Multi"):
        print("Enter a valid player count")
        return

   
    if difficulty == "Casual" and players == "Single":
        recommend("Watch Dogs \n MGRR")
    elif difficulty == "Casual" and players == "Multi":
        recommend("Finals")
    elif difficulty == "Pro" and players == "Single":
        recommend("Dark Souls")
    else:
        recommend("CSGO")

main()
