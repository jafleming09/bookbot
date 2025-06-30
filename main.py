def get_book_text (filepath):
    #print("in get_book_text")
    with open(filepath) as f:    
        return f.read()

def count_words(book_text):
    #print("in count_words")
    split_text = book_text.split()
    num_words = len(split_text)
    print (num_words, "words found in the document")

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_words(book_text)
    

main()
