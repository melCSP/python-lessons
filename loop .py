word_list = ["advark","baboon","camel"]

import random

choisen_word = random.choice(word_list)

guess = input ("guess a latter:").lower()

for letter in choisen_word:
   if letter == guess:
      print("right")
   else:
      print ("wrong")