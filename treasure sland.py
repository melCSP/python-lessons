print ("welcome to tresure sland")
print ("your mission is to find the tresure")

choice1 = input ('you \'re at a crossroad, where do you want to go? type "left" of "right"')
if choice1 == "left":
    choice2 = input('you\'ve come to a lake. there is an sland in the middle of lake. type "wait" to wait for a boat. type "swin" to swin cross ').lower()
    if choice2 == "WAIT" :
       choise3 = input("you arrive at the island unharmed. There is a house with 3 doors. One re, one yellow and one blue.wich colour do you choose").lower()
       if choise3 == "red":
          print("it's a room full of fire. game over")
       elif choise3 == "yes":
          print("you find treasure")
       elif choise3 =="blue":
          print("you enter a room of beasts. gaem over")
       else:
          print("you choose as door that doesn't exist.")
    else:
       print("you got attacked by angry trout.game over")
else:
       print("you fell into a hole. Game over")
