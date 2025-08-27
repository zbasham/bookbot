

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = word_count(book)
    characters = character_count(book)
    print(f"{num_words} words found in the document")
    print(characters)


# Gets the text from a specified book
def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

# Accepts a string 
# Uses the text from the book specified in get_book_text to give a word count.
from stats import word_count

from stats import character_count
main()