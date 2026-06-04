full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif character_name == '':
        return 'The character should have a name'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif ' ' in character_name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
        STR = (strength * full_dot) + ((10 - strength) * empty_dot)
        INT = (intelligence * full_dot) + ((10 - intelligence) * empty_dot)
        CHA = (charisma * full_dot) + ((10 - charisma) * empty_dot)

        return f'{character_name}\nSTR {STR}\nINT {INT}\nCHA {CHA}'


print(create_character('ren', 1, 2, 4))