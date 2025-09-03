def main():
    n = get_num()
    meow(n)

def get_num():
    while True:
        num = int(input("Enter a number: "))
        if num>0:
            break
    return num

def meow(num):
    for _ in range (num):
        print ("Meow")
main()

 