import sys
from stats import get_each_character_count, get_word_count, sort_stats

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1);
    num_words = get_word_count(get_book_text(sys.argv[1]))
    num_chars = get_each_character_count(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sort_stats(num_chars).items():
        if (key.isalpha()):
            print(f"{key}: {value}")
    print("============= END ===============")

main()
