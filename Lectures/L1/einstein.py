def main():
    value = int(input("Type any value as kilogram: "))
    converted_joules = convert(value)
    print(converted_joules)

def convert(number):
    c = 299792458
    return number * (c ** 2)
    

main() 
    