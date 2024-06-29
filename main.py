def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        sorted_char_count = sort_chars_dict(char_count)
        generate_report(sorted_char_count, word_count, book)

def count_words(content):
    
    words = content.split()
    count = 0

    for i in words:
        count += 1

    return count

def count_characters(content):
    chars_dict = {}

    for i in content:
        lowered = i.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1

    return chars_dict
    
def generate_report(sorted_chars, word_count, book_name):
    print(f"--- Report of {book_name} ---\n{word_count} words found")
    

    for i in sorted_chars:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times.")

    print("--- End Report ---") 


def sort_on(dictionary):
    return dictionary['num'];

def sort_chars_dict(chars):
    word_list = []
    for char in chars:
        word_list.append({"char": char, "num": chars[char]})

    word_list.sort(reverse=True, key=sort_on)
    return word_list

main()
