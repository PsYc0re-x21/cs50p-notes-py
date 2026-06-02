def main():
    type= input ("Type anything with either ':)' or ':(' ")
    converted_symbol = convert(type)
    print(converted_symbol)

def convert (text):
    if ":)" in text:
        return text.replace(":)", "🙂")
    elif ":(" in text:
        return text.replace(":(", "🙁")
    else:
        return text
    
main()