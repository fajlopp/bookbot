def main():
    book_path = "books/frankenstein.txt"
    try:
        text = get_book_text(book_path)
        count_words = count_words_in_file(text)
        print(count_words)
    except FileNotFoundError:
        print(f"Error: The file {book_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def count_words_in_file(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()