def get_book_text (filepath):
    #print("in get_book_text")
    with open(filepath) as f:    
        return f.read()

from stats import count_words #from name of file without .py import function to import

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count_words(book_text)
    

main()
