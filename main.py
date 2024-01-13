# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

	# for windows
  if name == 'nt':
    _ = system('cls')

	# for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')


import random

from hangman_art import stages, logo
from hangman_words import words_list

with open("parole.txt", "r") as tf:
  words_list = tf.read().split("\n")

print(logo)
selected_word = random.choice(words_list)
hidden_word = []
for _c in selected_word:
  hidden_word += "_"

end_of_game = False
lives = 6
print(f"\n\nIndovina la seguente parola da {len(selected_word)} caratteri:")
print(f"{' '.join(hidden_word)}")
print(stages[lives])
while not end_of_game:
  char_guess = input("Digita il carattere: ").lower()
  clear()
  if char_guess in hidden_word:
    print(f"Hai già inserito il carattere {char_guess}!")

  if char_guess not in selected_word:
    print(f"Il carattere {char_guess} non è nella parola. Perdi una vita!")
    lives -= 1
  for position in range(len(selected_word)):
    
    if char_guess==selected_word[position]:
      hidden_word[position]=char_guess
    
      
  print(f"{' '.join(hidden_word)}")
  print(stages[lives])
  
  if "_" not in hidden_word:
    end_of_game = True
    print("Hai Vinto!")

  if lives == 0:
    end_of_game = True
    print(f"Hai Perso!\nLa parola era: {selected_word}")
