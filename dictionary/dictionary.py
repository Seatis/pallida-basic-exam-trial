dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word):
    dictionary.append({hun_word: eng_word})
    print (dictionary)

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'

def key_list_maker():
    key_list = []
    for i in range(len(dictionary)):
        key_list += [(list(dictionary[i].keys())[0])]
    return key_list

def translate_to_hun(eng_word):
    keys = key_list_maker()
    i = 0
    for line in dictionary:
        if line[keys[i]] == eng_word:
            return keys[i]
        i += 1

def translate_to_eng(hun_word):
    keys = key_list_maker()
    i = 0
    for line in dictionary:
        if keys[i] == hun_word:
            return line[keys[i]]
        i += 1


# add_word("asztal", "desk")
print(translate_to_hun("tree"))
print(translate_to_eng("fa"))