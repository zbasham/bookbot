def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    chars_list = list(chars_dict)
    for letter in range(len(chars_list)):
        if chars_list[letter].isalpha() == True:
            print(f"The {chars_list[letter]} character was found {chars_dict[chars_list[letter]]}")
    print("--- END REPORT ---")


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    




main()