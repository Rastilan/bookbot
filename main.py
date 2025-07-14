from stats import count_words;

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();

    print(file_contents);

#main();
