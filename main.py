from stats import *
import sys

def main():
    file_path="./books/frankenstein.txt"
    
    file_contents=get_books_text(file_path)

    words=file_contents.split()

    num_words=count_words(words)
    print(f"""============ BOOKBOT ============
    Analyzing book found at {file_path}
    ----------- Word Count ----------""")

    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    x=list(words)
    y=[]


    lower=lower_case(file_contents)

    counted_char_dict=count_char(lower)
    
    converted_dict_list=conversion_dict(counted_char_dict)
    

    sorted_dict_list=sort(converted_dict_list)
    

    sorted=return_dict_from_list(sorted_dict_list)

    return sorted
print(main())