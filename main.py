from stats import count_words #from name of file without .py import function to import
from stats import count_chars
from stats import lower_convert
from stats import string_split

def get_book_text (filepath): #opens and reads file
    with open(filepath) as f:    
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt") #calls and passes file directory
    count_words(book_text) #not needed at this time
    lower_case = lower_convert(book_text) #convert all characters to lowercase
    split_string = string_split(lower_case) #split words into individual strings
    count_chars(split_string) #count characters in each word string, incrementing counter
    

main()
