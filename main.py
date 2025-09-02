import sys
from stats import (count_words,
                   count_characters,
                   count_characters_sorted)
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    num_words = count_words(contents)
    chars_dict = count_characters(contents)
    sorted_chars_list = count_characters_sorted(chars_dict)
    print_report(book_path, num_words, sorted_chars_list)


def print_report(book_path, num_words, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
main()