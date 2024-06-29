def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        generate_report(char_count, word_count, book)

def count_words(content):
    
    words = content.split()
    count = 0

    for i in words:
        count += 1

    return count

def count_characters(content):
    chars_dict = {}

    for i in content:
        lowered = content.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1

    return chars_dict
    
def generate_report(alphabet, word_count, book_name):
    print(f"--- Report of {book_name} ---\n{word_count} words found")
    
    word_list = []
    for i in alphabet:
        char_dict = {alphabet[i]}
        word_list.append(char_dict);
    
    word_list.sort(reverse=True, key=sort_on)
    print(word_list)


def sort_on(dictionary):
    return dictionary[0];

main()
