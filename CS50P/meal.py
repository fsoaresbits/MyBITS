def main():
    meal_time = convert(input('What time is it? '))

    if 7.0 <= meal_time <= 8.0:
        print('breakfast time')
    elif 12.0 <= meal_time <= 13.0:
        print('lunch time')
    elif 18.0 <= meal_time <= 19.0:
        print('dinner time')
    else:
        pass


def convert(time):
    hours, minutes = time.split(':')
    converted_time = float(hours) + (float(minutes) / 60)
    return converted_time

if __name__ == "__main__":
    main()
