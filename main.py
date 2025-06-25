import sys
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    #print(f"{num_words} words found in the document")

    num_characters = get_num_characters(book_text)
    sorted_list = get_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

main()