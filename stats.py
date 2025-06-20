def word_count(texts):
    words = texts.split()
    return len(words)

def char_count(texts):
    letters = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
        }
    formatted = texts.lower()
    for char in formatted:
        if char in letters:
            letters[char] += 1
    return letters

def d_conversion(character_dict):
    dictionary = []
    for entry in character_dict:
        number = character_dict[entry]
        # Create a NEW dictionary here
        new_dict = {"char": entry, "num": number}
        # Then append it to the list
        dictionary.append(new_dict)
    dictionary.sort(reverse=True,key=sort_on)
    return dictionary

def sort_on(dictionary):
    return dictionary["num"]