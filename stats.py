
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


def sort_chars(input):
    sorted_list = [];
    input = dict(sorted(input.items(), reverse=True, key=lambda key: key[1]))
    for key, value in input.items():
        if key== " ":
            pass
        else:
            sorted_list.append({"char": key, "num": value})
            
    return sorted_list
