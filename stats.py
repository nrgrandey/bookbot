# Function to count the amound of words in a string
def word_count(text):
    num_words = 0
    word_list = text.split()
    for word in word_list:
        num_words += 1
    return num_words

def character_count(text):
    invalid_characters = set(" ,.!?;\":'-_—()*0123456789•[]$#%\\/&“”’‘™")
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in invalid_characters:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]
def sort_dict(dict):
    dict_list = []
    for char in dict:
        dict_list.append({"char" : char, "num" : dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
