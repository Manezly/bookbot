def print_book_text():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = len(text.split())
    print("word count is:", word_count)

def count_characters():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowercase_text = text.lower()

    char_count = {}
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_character_count():
    chars = count_characters()
    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

print_character_count()
# print_book_text()
# get_num_words()