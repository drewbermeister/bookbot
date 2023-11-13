def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for c in range(0, len(STRING)):
        letter_count[STRING[c]] = 0

    #TODO
    working_text = text.lower()

    for i in range(0, len(working_text)):
        if working_text[i] in letter_count.keys() and working_text[i] in STRING:
            letter_count[working_text[i]] += 1

    return letter_count

STRING = "abcdefghijklmnopqrstuvwxyz"
with open("books/frankenstien.txt") as f:
    file_contents = f.read()
    print(file_contents)
    characters = count_letters(file_contents)

    print("--- Bring report of {f} ---")
    print(f"{count_words(file_contents)} word(s) found in the document")
    for i in range(0, len(characters)):
        print(f"The {STRING[i]} character was found {characters[STRING[i]]} times")
    print("--- End report ---")
#read_book()

