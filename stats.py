# Function to count the amound of words in a string
def word_count(text):
    num_words = 0
    word_list = text.split()
    for word in word_list:
        num_words += 1
    return num_words

def character_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict
