
# Accepts a string 
# Uses the text from the book specified in get_book_text to give a word count.
def word_count(text):
    list_of_words = text.split()
    total_words = len(list_of_words)
    return total_words

# sample = "Please! Count my characters! :)"

def character_count(text):
    characters = {}
    for i in text:
        i = i.lower()
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    return characters
            