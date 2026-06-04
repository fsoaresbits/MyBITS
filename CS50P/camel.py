def main():
    camel_case = str(input("camelCase: "))

    snake_case = ""

    for i in range(len(camel_case)):
        if i == 0:
            if camel_case[i].isupper():
                snake_case = camel_case[i].lower()
            else:
                snake_case = camel_case[i]
        elif i > 0 and i < (len(camel_case) - 1):
            if camel_case[i].isupper():
                snake_case = snake_case + "_" + camel_case[i].lower()
            else:
                snake_case = snake_case + camel_case[i]
        else:
            snake_case = snake_case + camel_case[i]

    print(f"snake_case: {snake_case}")


main()
