greetings = input("Hi there!").strip().lower().startswith()
match greetings:
    case "hello":
        print("$0")

    case "h":
        print("$20")

    case _:
        print("$100")

#------~~~~~~~~~--------#

def main():
    # 1. Prompt for input, strip whitespace, and force lowercase
    # (Using a simple "Greeting: " prompt is safest for check50)
    greeting = input("Greeting: ").strip().lower()

    # 2. Check if the exact starting letters are "hello"
    if greeting.startswith("hello"):
        print("$0")
        
    # 3. Check if it starts with just "h"
    # (Since we used elif, this only runs if it IS NOT "hello")
    elif greeting.startswith("h"):
        print("$20")
        
    # 4. If it starts with anything else, Kramer gets the full $100
    else:
        print("$100")


# Start the program
main()
              
    