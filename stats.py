def count_words(book_text):
    #print("in count_words")
    split_text = book_text.split()
    num_words = len(split_text)
    print (num_words, "words found in the document")