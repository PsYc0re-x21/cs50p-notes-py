def main():
    names = [ "Mario" , "Daisy", "Luigi", "Yoshi"]
    for name in names:
        print (write_letter(name, "Princess Peach"))

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