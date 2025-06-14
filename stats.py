def word_count(text):
    num_words = 0
    word_list = text.split()
    for word in word_list:
        num_words += 1
    return num_words
