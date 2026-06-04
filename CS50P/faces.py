def convert(emoticons):
    return str(emoticons).replace(':)', '🙂').replace(':(', '🙁')


def main():
    print(convert(input()))


main()
