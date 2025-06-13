import sys
from stats import get_num_words
from stats import character_count
from stats import sort

def get_book_text(path):
    with open (path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    counts = character_count(text)
    character_count_sort = sort(counts)

    for char in character_count_sort:
        char_letter = char["char"]
        if char_letter.isalpha():
            print(f"{char_letter}: {char['num']}")

    print("============= END ===============")

main()

