import sys

def main():
    try:
        book = get_book_text(sys.argv[1])
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = word_count(book)
    characters = character_count(book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_characters(characters):
        for key in i:
            if key.isalpha() == True:
                print(f"{key}: {i[key]}")
            else:
                pass
    print("============= END ===============")



# Gets the text from a specified book
def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

# Accepts a string 
# Uses the text from the book specified in get_book_text to give a word count
from stats import word_count

# Accepts a string
# Creates a dictionary of every character in the book
from stats import character_count

# Accepts a dictionary of key=int(value) pairs
# Returns a list of dictionaries of the characters in the book
# The characters are sorted from most used to least used
from stats import sorted_characters

main()