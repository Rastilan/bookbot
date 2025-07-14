
def count_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words

def count_chars(contents):
    chars = {}
    for word in contents:
        for letter in word:
            letter = letter.lower()
            if letter in chars:
                chars[letter] += 1
            
            else:
                chars[letter] = 1
                
    return chars


