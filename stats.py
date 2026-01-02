def get_books_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
    return file_contents

def count_words(words):
    count=0
    for i in words:
        count+=1
    return count

def lower_case(words):
    lower=words.lower()
    return lower
    
def count_char(lower):
    char_dict={}
    for i in lower:
        if i.isalpha():
        
            if i in char_dict:
                char_dict[i]+=1
            else:
                char_dict[i]=1




    return char_dict
def alpha_only(char_dict):
    for char, count in sorted_chars:
        if char.isalpha(): # Optional: only print letters
            print(f"The '{char}' character was found {count} times")
def conversion_dict(char):
    l_dict=[]
    
    for i in char.keys():
        d=dict()
        d["char"]=i
        d["num"]=char[i]
        l_dict.append(d)
    return l_dict
def sort(l_dict):
    l_dict.sort(reverse=True, key=sort_on)
    return l_dict
def sort_on(l_dict):
    return l_dict["num"]
def return_dict_from_list(sorted_dict_list):
    for i in sorted_dict_list:
        character=i["char"]
        (frequency)=i["num"]
        print(character+": "+str(frequency))
    return " "


                
            
        