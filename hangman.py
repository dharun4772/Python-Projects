import hangman_words as hw
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
import random
word_list = hw.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word=word_list[random.randint(0,len(word_list)-1)]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=["_"]*len(word)
already=[]
print(logo)
count=len(stages)
f=0
while(count!=0):
  letter=input("Guess a letter?\n")
  if letter in already:
    print("You have guessed this already,try a different one")
    continue
  already.append(letter)
  if(letter in word):
    for i in range(len(word)):
      if(letter==word[i]):
        guess[i]=letter
    print("".join(guess))
    if("_" not in guess):
      print("WON")
      break
  else:
    print("".join(guess))
    print(stages[count-1])
    count-=1
if(count==0):
  print("LOST")
