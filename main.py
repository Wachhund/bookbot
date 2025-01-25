def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char.isalpha():  # Nur Buchstaben zählen
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(word_count, char_count_sorted):
    for entry in char_count_sorted:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
        
def sort_characters(char_count):
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list

def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)

    print(f"Die Anzahl der Wörter im Buch 'Frankenstein' beträgt: {word_count}")
    
    character_count = count_characters(file_contents)
    char_count_sorted = sort_characters(character_count)

    print_report(word_count, char_count_sorted)

main()