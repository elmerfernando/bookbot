def count_words(contents):
    num_words = contents.split()
    return len(num_words)

def count_characters(contents):
    number_characters = {}
    for ch in contents:
        lowered = ch.lower()
        if "a" <= lowered <= "z":
            if lowered in number_characters:
                number_characters[lowered] += 1
            else:
                number_characters[lowered] = 1
    return number_characters

def sort_on(items):
    return items["num"]

def count_characters_sorted(num_characters):
    character_list = []
    for ch, count in num_characters.items():
        character_list.append({"char": ch, "num": count})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
