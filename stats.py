def get_number_of_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words += 1
    message = f"Found {num_words} total words"
    return message

def get_char_count(book_text):
    words = book_text.lower().split()
    char_count = {}
    for word in words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sort_dict(char_count):
    sort_dictionary = []
    for key in char_count:
        sort_dictionary.append({"char": key, "num": char_count[key]})
    sort_dictionary.sort(reverse=True, key=sort_on)
    return sort_dictionary
