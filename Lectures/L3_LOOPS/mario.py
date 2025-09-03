def main():
    n= int(input("Please enter height: "))
    p= int(input("Please enter width: "))
    print_rectangle(n, p)

def print_rectangle(height, width):
    for i in range(height):
        print("#" * width)

main()