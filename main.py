from stats import count_words, count_chars
file_contents = ""
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        print(f'{word_count} words found in the document')
        print(char_count)


main();