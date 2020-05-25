import random

def display_letter(letter, guesses):
    if letter in guesses:
        return letter
    else: 
        return "_"  
     

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

def grab_guess():
    guess = input("Guess a letter: ").upper().strip()  
    return guess  

def guess_input(guess, current_guesses):   
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(guess) >= 2 or guess == "":
        print("Enter a single letter")
        grab_guess()
    elif guess in current_guesses:
        print("You've already entered that letter")
        grab_guess()
    elif guess not in alphabet:
        print ("Character entered is not a letter")   
        grab_guess()
    else:         
        return guess 


def game_loop(words, current_guesses):
    
    guess_count = 8 
    output = [] 
    while guess_count != 0:
        if output != words:
            guess = grab_guess()
            letter = guess_input(guess, current_guesses)
            check = check_letter(words, letter) 
            current_guesses.append(letter) 
            for letter in words:
                output.append(display_letter(letter, current_guesses))
        print(output) 
        if check == True:
            print("You guessed the correct letter!")
            print(f"You have {guess_count} guesses left") 
        else:
            print("You guessed the wrong letter. Try again!") 
            guess_count -= 1 
            print(f"You have {guess_count} guesses left")   
        if output == words: 
            print("You won the game!") 
            play_again()
        output = [] 
        if guess_count == 0:
            print("You lost the game")
            play_again()          
            
def play_again():  
    play_again = input("Do you want to play again? Y or N? ")
    if play_again == "Y" or "y": 
        play_game()  
    elif play_again == "N" or "n":
        raise SystemExit           

        

def check_letter(words, letter):  
    if letter in words: 
        return True 
    else:
        return False 
            

    



    

def play_game (): 
    words = clean_text()
    current_guesses = []
    game_loop(words, current_guesses) 


        



          

play_game() 


















# def easy_words(words):
#     easy_words = []
#     for word in words:
#         if len(word) >= 4 and len(word) <=6:
#             easy_words.append(word)
#     return easy_words 
#     print (easy_words) 
   


# def normal_words(words):
#     normal_words = []
#     for word in words:
#         if len(word) >= 6 and len(word) <= 8:
#             normal_words.append(word)
#     return normal_words   
 

# def hard_words(words):
#     hard_words = []
#     for word in words:
#         if len(word) >= 8:
#             hard_words.append(word)
#     return hard_words  


# def input_option(prompt, options):
#     while True:
#         try:
#             str_input = input(prompt)
#             if str_input not in options:
#                 raise ValueError
#             return str_input
#         except ValueError:
#             print ("That is not a valid input")
#         else:
#             return difficulty         
# difficulty = input_option("What level do you want to play on? (E)asy, (M)edium, or (H)ard? ", ["E", "M", "H"])            


# def make_mystery_word(difficulty):
#     if difficulty == "E":
#         return (easy_words(get_word()))

#     elif difficulty == "N":
#             return (normal_words(get_word()))

#     elif difficulty == "H":
#             return (hard_words(get_word()))  

# make_mystery_word(difficulty)                    
        







   


