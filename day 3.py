print ("tsank you choosing python pizza delivery ")
size = input () # what size pizza do you want? s,m, or l
add_pepperoni = input () #Do you want pepperoni ? y or N
extra_cheese = input ()

bill = 0
if size == "s" :
    bill +=15
elif size == "m":
    bill += 20
else:
    bill += 25
    if add_pepperoni == "y":
        if size == "s":
            bill += 2
        else:
            bill += 3
if extra_cheese == "y":
    bill += 1

print("you final bill is: $(bill)")
