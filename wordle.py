from random_word import RandomWords
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from IPython.display import display

def pick_random_word():
    #Instantiate randomizer
    r = RandomWords()
    
    true_word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minDictionaryCount = 3, minLength=5, maxLength=5)

    while true_word == None or '-' in true_word:
        true_word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minDictionaryCount = 3, minLength=5, maxLength=5).upper()
    else:
#         print(f'Word is: {true_word}')
        return true_word

#Ask User Input
def ask_user_input(guru = None):
    while True:
        guru = input ("Enter a 5-letter Word :")
        if type(guru) != str or len(guru) != 5:
            print('Invalid Entry')
            continue
        else:
            return guru.upper()

#Change Letter Colors
def color_positive(val):
    if val == val.upper() and len(val) == 1:
        color = 'green'
    elif len(val) == 2:
        color = 'orange'
    else:
        color = 'black'
    return 'color: %s' % color

def build_df(attempt, guess_arr):
    cols = ['L1', 'L2', 'L3', 'L4', 'L5']
    idx = ['TRY_' + str(attempt +1)]
    
    df = pd.DataFrame(guess_arr).T
    df.columns = cols
    df.index = idx
    
    return df

def mark_letters(guess_idx):
    final = []
    for item in guess_idx:
        if item[2] == 'YES':
            final.append(item[0])
        elif item[2] == 'EX':
            final.append(item[0] + ' ')
        else:
            final.append(item[0].lower()) 
    return final

#############################################
############  MAIN FUNCTION ################
#############################################
def play_wordle():
    #Instantiate True word
    true_word = pick_random_word()
    
    #Turn true word into array of individual letters and indexes
    true_arr = np.array(list(true_word.upper()))
    # print(true_arr)
    true_idx = [[item, idx, None] for idx, item in enumerate(true_arr)]
    # print(true_idx)
    
    attempt = 0
    guess_store = []
    
    while attempt < 6:
        #guess word
        guess_word = ask_user_input()
        guess_arr = np.array(list(guess_word))
        # print(guess_arr)
        guess_idx = [[item, idx, None] for idx, item in enumerate(guess_arr)]
        # print(guess_idx)

        matched = []
        existing = []
        matching = np.where(true_arr == guess_arr)[0]

        for item in matching:
            matched.append(guess_idx[item][0])
            guess_idx[item][2], true_idx[item][2] = 'YES', 'YES'

        rem_guess = [item for item in guess_idx if item[2] != 'YES']
        rem_true = [item for item in true_idx if item[2] != 'YES']
        # print(rem_guess, rem_true)

        for guess in rem_guess:
            for true in rem_true:
                if guess[0] == true[0]:
                    if list(true_arr).count(guess[0]) > (matched.count(guess[0]) + existing.count(guess[0])):
                        existing.append(guess[0])
                        guess[2], true[2] = 'EX', 'EX'
                    else:
                        continue
        
        #Apply logic to each value in DataFrame to Color letters
        def color_positive(val):
            if val == val.upper() and len(val) == 1:
                color = 'green'
            elif len(val) == 2:
                color = 'orange'
            else:
                color = 'black'
            return 'color: %s' % color

        #Mark letters based on match, exist, or not exist
        final = mark_letters(guess_idx)
        
        #Turn current guess word into row in pandas DF
        guess_df = build_df(attempt, final)
        guess_store.append(guess_df)
        new_df = pd.concat(guess_store)
        
        #Use color_positive function to color letters
        s = new_df.style.applymap(color_positive)
        display(s)

        if guess_word.lower() == true_word:
            print('##############################################################')
            print(f'       HURRAY THE WORD WAS: {true_word.upper()} ')
            print('##############################################################')
            print('YOU ARE A HUMAN GENIUS! YOU SHOULD BE FEARED AND RESPECTED!!!')
            print('Give yourself a pat on the shoulder :)')
            print("That student debt is finally paying off!!!")
            print("WANNA PLAY AGAIN?")
            break
        else:
            attempt += 1
            
            if attempt == 6:
                print(f'Sorry, gotta read more BOOKS! The word was {true_word.upper()}, OBIOUSLY...')
                break

if __name__ == '__main__':
    play_wordle()
