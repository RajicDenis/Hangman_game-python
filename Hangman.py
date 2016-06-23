import string
import random

def load_words ():
    file=open('words.txt', 'r')
    words=file.readline()    
    text=str.split(words)
    return text

def random_word(text):
    return random.choice(text)

def partial (the_word, good_guess):
    end_word=""
    for letter in the_word:
        if letter in good_guess:
            end_word+="" + letter
        else:
            end_word += "_ "
    return end_word        

while True:
    key=True
    print ('\n\nWELCOME TO HANGMAN!\nThe rules are simple:\n1) You have 10 attempts to choose a letter and find\
 the correct answer\n2) After the first guessed letter you have 5 attempts to guess the complete word\n3)\
 If you run out of attempts you lose\n')
    num_let=0
    all_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']       
    the_word=random_word(load_words())
    print ('A random word has been chosen!')
    attempts=10
    fin_attempt=5
    guessed_w=False
    condi=True
    good_guess=""
    print ('You have ', attempts, 'attempts')

    for i in the_word:
        num_let += 1
    print ('The word has ', num_let, 'letters.')
    while attempts>0 and key==True:
        condi=True
        chosen_letter=str(input('Choose a letter: '))
        assert type(chosen_letter)==str and len(chosen_letter)==1
        if chosen_letter in all_letters and chosen_letter in the_word:
            good_guess+=chosen_letter
            print ('Good guess! ', partial(the_word, good_guess),'\n')
            all_letters.remove(chosen_letter)
            if partial(the_word, good_guess)!=the_word:
                print ('Remaining letters: ', all_letters, '\n')
            if partial(the_word, good_guess)==the_word:
                guessed_w=True
            if guessed_w==True:    
                print ('Correct! The final word is ', the_word, '. You have won!')
                restart=str(input('Do you want to restart the game? (Yes or No): '))
                key=False
        elif chosen_letter not in all_letters[:]:
            print ('You have already chosen that letter!\n')
            condi=False
        else:
            print ('Wrong! You have ', attempts-1,'attempts left!\n')
            all_letters.remove(chosen_letter)
            print ('Remaining letters: ', all_letters, '\n')
            attempts-=1
        if attempts>0 and fin_attempt>0 and condi==True:
            final_answer=str(input("You can try and guess the final answer (if you don't know type No): "))
            if final_answer==the_word:
                print ("Correct! The final word is ", the_word, ". You have won!")
                restart=str(input('Do you want to restart the game? (Yes or No): '))
                key=False
            elif final_answer=='No':
                assert True
            else:    
                fin_attempt-=1
                print ("Wrong answer! You have ", fin_attempt, " left\n")
        if attempts==0:
            print ('Wrong! You have lost the game!')
            restart=str(input('Do you want to restart the game? (Yes or No): '))
            key=False
    if restart=='No':
        assert False
    elif restart=='Yes':
        continue
        

                
