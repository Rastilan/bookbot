def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();
    words = file_contents.split();
    num_words = len(words);
    print(f'{num_words} words found in the document')

def count_chars():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();
        words = file_contents.split();
        for word in words:
            for letter in word:
                letter = letter.lower();
                if letter in char_count:
                    char_count[letter] += 1;
                
                else:
                    char_count[letter] = 1;
                
    print(char_count);


count_chars();