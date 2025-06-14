from stats import character_count, sort_dict, word_count


# Function to recieve a book's file path and output the contents in a string format
def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents

def main():
    char_dict = character_count(get_book_text("books/frankenstein.txt"))
    sorted_dict = sort_dict(char_dict)
    print("============ BOOKBOT ============\n----------- Word Count ----------")
    num_words = word_count(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
