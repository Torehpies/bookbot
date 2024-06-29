def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)

def count_words(content):
    
    words = content.split()
    count = 0

    for i in words:
        count += 1

    return count


main()
