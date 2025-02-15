def fetch_text():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        return(text)

def word_count():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        words = text.split()
        return(len(words))

def character_count():
    with open("books/frankenstein.txt") as file:
        character_dict = {}
        text = file.read()
        lower_text = text.lower()
        for character in lower_text:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        return(character_dict)
        
def alphabet_filter():
    filtered_dict = {}
    raw_dict = character_count()
    for character in raw_dict:
        if character.isalpha():
            filtered_dict[character] = raw_dict[character]
    return(filtered_dict)

def sort():
    filtered_dict = alphabet_filter()
    # Convert dictionary to a list of tuples and sort by value in descending order
    sorted_list = sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
    return(sorted_list)

def book_report():
    print("--- Begin report of books/frankenstein.txt ---")
    count = word_count()
    print(f"{count} found in this book")
    print()
    alphabet_count = sort()
    for character, count in alphabet_count:
        print(f"The '{character}' character was found {count} times")
    print("--- End of report ---")
    
def main():
        book_report()

main()