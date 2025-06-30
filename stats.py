def count_words(text): #counts how many words in book
    split_text = text.split()
    num_words = len(split_text)
    print (f'Found {num_words} total words')

def lower_convert(text): #sets all characters to lowercase
    return str.lower(text)

def string_split(text): #splits text into individual strings
    return text.split()

def count_chars(text): #counts individual characters, adds them to dictionary
    char_dict = {}
    for words in text:
        for char in words:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def dict_sort(dict_to_sort):
    dict_list = []
    for key, value in dict_to_sort.items():
        dict_list.append({"char":key, "num": value})
        dict_list.sort(reverse = True ,key=lambda item: item["num"])
    
    for item in dict_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

        #.sort(reverse=True, key=sort_on)
    #print(sorted_dict)



        
        
