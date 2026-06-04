def main():
    due = 50

    while due > 0:
        coin = int(input(f"Amount Due: {due}\nInsert Coin: "))

        if coin == 5 or coin == 10 or coin == 25:
            due -= coin

        if due <= 0:
            change = -due

            print(f"Change Owed: {change}")


main()
