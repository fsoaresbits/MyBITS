def main():
    plate = input("Plate: \n")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): # Main
    return (
        has_valid_start(s)
        and has_valid_length(s)
        and has_valid_numbers(s)
        and has_no_punctuation(s)
    )


def has_valid_start(s):
    # Must start with at least two letters.
    return s[0:2].isalpha()


def has_valid_length(s):
    # May contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    return len(s) >= 2 and len(s) <= 6


def has_valid_numbers(s):
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a ‘0’.

    if s.isalpha():
        return True
    else:
        for character in range(len(s)): # Get the first number and it's index.
            if not s[character].isalpha():
                first_number = s[character]
                first_number_index = character
                break

        last_character = s[len(s) - 1]
        last_character_index = len(s) - 1

        if not last_character.isalpha() and  s[len(s) - 2].isalpha():
            valid_number_position = False
        else:
            valid_number_position = (first_number_index != last_character_index) and not last_character.isalpha() and first_number != '0'

        return valid_number_position


def has_no_punctuation(s):
    # No periods, spaces, or punctuation marks are allowed.
    return s.isalnum()


main()
