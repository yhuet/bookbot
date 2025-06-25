def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = {}
    text = text.lower()

    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters

def sort_on(items):
    return items["num"]

def get_sorted_list(characters_dict):
    characters_list = []

    for char in characters_dict:
        characters_list.append({"char": char, "num" : characters_dict[char]})

    characters_list.sort(reverse=True, key=sort_on)

    return characters_list
