from stats import character_count, word_count


# Function to recieve a book's file path and output the contents in a string format
def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents

def main():
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    char_dict = character_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(char_dict)


main()
