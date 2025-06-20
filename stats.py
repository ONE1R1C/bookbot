def counting_words(word_count):
    with open(word_count) as text:
        words = text.read()
        count = len(words.split())
    return count

def letter_sum(path_to_file):
    letter_dict = {}
    unique = set()
    with open(path_to_file) as text:
        words = text.read().lower()
        for char in words:
            if char in unique:
                letter_dict[char] += 1
            elif char not in letter_dict:
                letter_dict[char] = 1
                unique.add(char)
    return letter_dict

def sort_key(key_name):
    return key_name["num"]

def sort_dict(dictionary):
    base_list = []
    
    for char in dictionary:
        if char.isalpha():
            iterate_list = {"char": char, "num":dictionary[char]}
            base_list.append(iterate_list)
    base_list.sort(reverse=True, key=sort_key)

    for i in range(0, len(base_list)):
        printed = base_list[i]
        printed_char = printed["char"]
        printed_num = printed["num"]
        print(f"{printed_char}: {printed_num}")
    return