def main():
    book_path = "books/frankenstein.txt"
    try: 
        print(f"--- Begin report of {book_path} ---")
        text = get_book_text(book_path)
        count_words = count_words_in_file(text)
        count_characters = count_characters_in_file(text)
        print(f"{count_words} words found in the document\n")
        char_report = print_character_report(count_characters)
        print("--- End report ---")
    except FileNotFoundError:
        print(f"Error: The file {book_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def count_words_in_file(text): # Splits the text into words and counts them.
    words = text.split()
    return len(words)

def get_book_text(path): # Reads the text from the given file path.
    with open(path) as f:
        return f.read()

def count_characters_in_file(text): # Counts occurrences of each alphabetic character.
    character_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_on(count_characters): # Returns the count part of the dictionary for sorting.
    return count_characters["num"]

def print_character_report(count_characters): # Converts the character counts to a sorted list of dictionaries and prints a formatted report.
    list_of_dict = []
    for character in count_characters:
        list_of_dict.append({"character": character, "num": count_characters[character]})
    list_of_dict.sort(reverse=True, key=sort_on)
    for sentence in range(len(list_of_dict)):
        print(f"The '{list_of_dict[sentence]['character']}' character was found {list_of_dict[sentence]['num']} times")

main()