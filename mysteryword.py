import random

           

def get_word():
    with open("words.txt") as words_list:
        words = words_list.readlines()
        return (random.choice(words)) 
     

def clean_text():
    new_word = get_word()
    upper_word = new_word.upper()
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_list = [] 
    for char in upper_word:
        if char in all_letters:
            word_list.append(char)
    print(word_list)        
    return word_list 

# clean_text()    

def easy_words(words):
    easy_words = []
    for word in words:
        if len(word) >= 4 and len(word) <=6:
            easy_words.append(word)
    return easy_words 
   


def normal_words(words):
    normal_words = []
    for word in words:
        if len(word) >= 6 and len(word) <= 8:
            normal_words.append(word)
    return normal_words   
 

def hard_words(words):
    hard_words = []
    for word in words:
        if len(word) >= 8:
            hard_words.append(word)
    return hard_words  


def input_option(prompt, options):
    while True:
        try:
            str_input = input(prompt)
            if str_input not in options:
                raise ValueError
            return str_input
        except ValueError:
            print ("That is not a valid input")
        else:
            return difficulty         
difficulty = input_option("What level do you want to play on? (E)asy, (M)edium, or (H)ard? ", ["E", "M", "H"])            


def make_mystery_word(difficulty):
    if difficulty == "E":
        return (easy_words(get_word()))

    elif difficulty == "N":
            return (normal_words(get_word()))

    elif difficulty == "H":
            return (hard_words(get_word()))  

make_mystery_word(difficulty)                    
        











# def display_guesses(mystery_word, guesses):
#     for letter in mystery_word:
#         if letter in correct_guesses:
#             print(letter.upper(), end=" ")
#         else: 
#             print("_", end=" ")    


