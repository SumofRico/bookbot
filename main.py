def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_chars_dict = get_chars_list_dicts(chars_dict)

    # print(get_report(chars_dict))
    # print(f"{num_words} words found in the document")
    list_chars_dict.sort(reverse=True, key=sort_on)
    # print(report(book_path, num_words, list_chars_dict))
    # for key in chars_dict: 
    #     print(f"key: {key} value: {chars_dict[key]}")


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


# def report(path, num_words, sorted_list):
#     print(f"--- Begin report of {path} ---")
#     print(f"{num_words} words found in the document\n")

#     print(sorted_list.sort(reverse=True, key="num"))
#     # for i in sorted_list:
#         # print(i)
# # list_chars_dict.sort(reverse=True, key=sort_on))
#     print("--- End report ---")


    

main()
