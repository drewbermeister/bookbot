def read_book():
    with open("/github.com/drewbermeister/bookbot/books/frankenstein.txt") as f:
        file_context = f.read()
        print(file_context)

        count_words(file_context)
        f.close()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("hello world!")
    #read_book()

