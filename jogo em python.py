import random


word_list = ["arvard", "baboon", "camel"]

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


end_of_game = False
lives =  6

from hangman_art import logo, stages 
print (logo)

print (f'pssst, the solution is {chosen_word}')

display = []

for _ in range (word_length):
    display += "_"

    while not end_of_game:
        guess = input ("guess a letter :").lower()

        if guess in display:
            print (f"you've already guessed {guess}")

        for position in range (word_length):
            letter = chosen_word[position]
            print (f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

                if guess not in chosen_word:
                    print(f"you guessed {guess}, tha's not in the word. you lose a life")
                    lives -= 1
                    if lives == 0:
                        end_of_game = print ("you lose")

                        print (f"{''.join(display)}")

                        if "_" not in display:
                            end_of_game = True
                            print ("you win")

 
                            print (stages[lives])