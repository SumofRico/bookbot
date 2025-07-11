import sys
from stats import get_number_of_words
from stats import get_char_count
from stats import get_sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    number_of_words = get_number_of_words(book_text)
    char_count = get_char_count(book_text)
    sort_dict = get_sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(number_of_words)
    print("--------- Character Count -------")
    for dict in sort_dict:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()
