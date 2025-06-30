def count_words(text): #counts how many words in book
    split_text = text.split()
    num_words = len(split_text)
    print (num_words, "words found in the document")

def lower_convert(text): #sets all characters to lowercase
    return str.lower(text)

def string_split(text):
    return text.split()

def count_chars(text):
    char_dict = {}
    for words in text:
        for char in words:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    print (char_dict)




        
        
