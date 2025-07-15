from stats import count_words, count_chars, sort_chars
import sys

def main():

    if len(sys.argv) > 1:
        book_location = sys.argv[1]
        file_contents = ""
        with open(book_location) as f:
            file_contents = f.read()
            word_count = count_words(file_contents)
            char_count = count_chars(file_contents)
            
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {book_location}...")
            print("----------- Word Count ----------")
            print(f'Found {word_count} total words')
            print("--------- Character Count -------")
            char_sort = sort_chars(char_count)
            for item in char_sort:
                if not item["char"].isalpha():
                    continue
                print(f"{item["char"]}: {item['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()