def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_chars_dict = get_chars_list_dicts(chars_dict)

    list_chars_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for i in list_chars_dict:
        if i["name"].isalpha():
            char = i["name"]
            occurance_num = i["num"]
            print(f"The {char} character was found {occurance_num} times")
    print("--- End report ---")

def get_book_text(path): 
    with open(path) as f:
        return f.read()
    
def get_num_words(text): 
        words = text.split()
        return len(words) 

def get_chars_dict(text): 
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars 

def get_chars_list_dicts(dict):
    dict_sort_prep = []

    for key in dict:
        key_value = {"name": key, "num": dict[key]}
        dict_sort_prep.append(key_value)
    
    return dict_sort_prep

def sort_on(dict):
    return dict["num"]
    

main()
