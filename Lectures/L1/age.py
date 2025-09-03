def get_age():
    age = int(input ("Enter a number: "))
    return age
def main():
    num = get_age()
    if num>=21:
        print("You are old enough")
    else:
        print("Nope!")
        
main()