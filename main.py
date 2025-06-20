import sys
from stats import (
    counting_words,
    letter_sum,
    sort_dict,
)

def get_book_text(path_to_file):
    with open(path_to_file) as text:
        book_contents = text.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    total_words = counting_words(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    total_letters = letter_sum(sys.argv[1])
    sort_sort = sort_dict(total_letters)
    print("============= END ===============")

main()