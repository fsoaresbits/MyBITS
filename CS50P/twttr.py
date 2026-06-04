def main():
    string = input("Input: ")

    shrtn = ""

    for letter in range(len(string)):
        LETTER_A = string[letter].upper() != "A"
        LETTER_E = string[letter].upper() != "E"
        LETTER_I = string[letter].upper() != "I"
        LETTER_O = string[letter].upper() != "O"
        LETTER_U = string[letter].upper() != "U"

        if LETTER_A and LETTER_E and LETTER_I and LETTER_O and LETTER_U:
            shrtn += string[letter]

    print(shrtn)


main()
