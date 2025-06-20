import sys
from stats import word_count
from stats import char_count
from stats import sort_on
from stats import d_conversion

def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content

def main():
    args = sys.argv 
    if len(args) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    real_path = args[1]
    book_text = get_book_text(real_path)
    character_dict = char_count(book_text)
    total_words = word_count(book_text)
    sorted_d = d_conversion(character_dict)
    #Print Lines
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {real_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_d:
        if item['char'].isalpha():
          print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()