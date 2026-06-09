def main():
    time = input("What time is it?").strip()

    floating_time = convert(time)

    if 7.0 <= floating_time <= 8.0:
        print("Breakfast time!")
    elif 12.0 <= floating_time <= 14.0:
        print("Lunch time!")
    elif 18.0 <= floating_time <= 20.0:
        print("Dinner time!")
    else:
        print("Invalid meal time!")
    


def convert(time):
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes= float(minutes)


    return hours + (minutes/60)


if __name__ == "__main__":
    main()