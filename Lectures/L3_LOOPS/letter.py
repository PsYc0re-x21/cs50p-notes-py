def main():
    names = [ "Mario" , "Daisy", "Luigi", "Yoshi"]
    for i in range (len(names)):
        print (write_letter(names[i], "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},
        You are invited to the party at 7PM!

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
main()