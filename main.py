from stats import count_words #from name of file without .py import function to import
from stats import count_chars
from stats import lower_convert
from stats import string_split
from stats import dict_sort
import sys

def get_book_text (filepath): #opens and reads file
    with open(filepath) as f:    
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print('===============BOOKBOT==================')
    print(f'Analyzing book found at {filepath}')
    print('------------ Word Count -------------')
    book_text = get_book_text(filepath) #calls and passes file directory
    count_words(book_text) # counts words in the text
    lower_case = lower_convert(book_text) #convert all characters to lowercase
    split_string = string_split(lower_case) #split words into individual strings
    counted_chars = count_chars(split_string) #count characters in each word string, incrementing counter
    print('----------- Character Count -----------')
    dict_sort(counted_chars) #turns dictionary into list and reverse sorts by value
    

main()
