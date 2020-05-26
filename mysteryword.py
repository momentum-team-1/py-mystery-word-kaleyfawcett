import random

def display_letter(letter, guesses):
    if letter in guesses:
        return letter
    else: 
        return "_"  
     

def get_word():
    with open("words.txt") as words_list:
        words = words_list.readlines() 
        return words 
   
     

def clean_text():
    new_word = choose_difficulty()
    upper_word = new_word.upper()
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_list = [] 
    for char in upper_word:
        if char in all_letters:
            word_list.append(char)        
    return word_list 


def choose_difficulty():
    new_word_list = get_word()
    level = input("What difficulty would you like to play on? (E)asy, (N)ormal, or (H)ard? ") 
    new_word_levels = []
    if level == "E":
        for entries in new_word_list:
            if len(entries) >= 4 and len(entries) <= 6:
                new_word_levels.append(entries) 
    if level == "N":
        for entries in new_word_list:
            if len(entries) >= 6 and len(entries) <= 8:
                new_word_levels.append(entries) 
    if level == "H":
        for entries in new_word_list:
            if len(entries) >= 8:
                new_word_levels.append(entries)                       

    return(random.choice(new_word_levels))      


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
            print("Congrats! You won the game!") 
            play_again()
        output = [] 
        if guess_count == 0:
            print("I am sorry, you are out of guesses. The word was: ", words)
            play_again()          
            
def play_again():  
    play_again = input("Do you want to play again? Y or N? ")
    if play_again == "Y" or play_again == "y": 
        play_game()  
    elif play_again != "Y" or play_again != "y": 
        raise SystemExit          

        

def check_letter(words, letter):  
    if letter in words: 
        return True 
    else:
        return False 
            

    
def start_game ():
    print("")
    print("Welcome to Mystery Word Game!")
    print("")


    

def play_game (): 
    start_game() 
    words = clean_text()
    print(f"Your word is {len(words)} letters long!")
    current_guesses = []
    game_loop(words, current_guesses) 




if __name__ == "__main__":
    play_game()

