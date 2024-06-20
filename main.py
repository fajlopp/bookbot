def main():
    book_path = "books/frankenstein.txt"
    try: 
        text = get_book_text(book_path)
        count_words = count_words_in_file(text)
        count_characters = count_characters_in_file(text)
        print("Word count:", count_words)
        print("Character count:", count_characters)
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

def count_characters_in_file(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
main()