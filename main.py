def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_characters(file_contents)

def count_words(content):
    
    words = content.split()
    count = 0

    for i in words:
        count += 1

    return count

def count_characters(content):
    content = content.lower()
    alphabet = {"a":0,"b":0,"c":0,"d":0,"e":0,
                "f":0,"g":0, "h":0, "i":0, "j":0,
                "k":0, "l":0, "m":0, "n":0, "o":0,
                "p":0, "q":0, "r":0, "s":0, "t":0,
                "u":0, "v":0, "w":0, "x":0, "y":0,
                "z":0}
    words = content.split()

    for i in words:
        for j in i:
            for k in alphabet:
                if j == k:
                    alphabet[k] += 1

    print(alphabet)
    


main()
