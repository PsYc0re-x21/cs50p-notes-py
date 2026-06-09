def main():
    values = input("Expression: ")

    
    x, y, z = values.split(" ")

    x = float(x)
    z = float(z)

   
    result = calculate(x, y, z)

    print(f"{result:.1f}")


def calculate(x, y, z):
   
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z



main()