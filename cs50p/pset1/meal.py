def main():
    time = input("What time is it? ")
    time_formatted = convert(time)
    if 7 <= time_formatted <= 8:
        print("breakfast time")
    if 12 <= time_formatted <= 13:
        print("lunch time")
    if 18 <= time_formatted <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    time_formatted = hours + minutes
    return time_formatted



if __name__ == "__main__":
    main()
