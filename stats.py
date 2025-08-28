
# Accepts a string 
# Uses the text from the book specified in get_book_text to give a word count.
def word_count(text):
    list_of_words = text.split()
    total_words = len(list_of_words)
    return total_words

sample = "Please! Count my characters! :)"

def character_count(text):
    characters = {}
    for i in text:
        i = i.lower()
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    return characters

# Sorts a dictionary into new, single key:value dictionaries from greatest to smallest

def sorted_characters(char_dict):
    list_of_dicts = []
    for i in char_dict:
        small_dict = {}
        small_dict[i] = char_dict[i]
        list_of_dicts.append(small_dict)
        list_of_dicts.sort(reverse = True, 
            key = lambda each_dict: list(each_dict.values())[0]
            )
    return list_of_dicts


#Test
sorted_characters(character_count(sample))