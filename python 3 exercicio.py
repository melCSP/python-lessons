print("welcome to the rollecuster")
height = int(input("what is yout heigth in cm?"))

if height >=120:
    print ("you can ride the rollercoaster")
    age = int(input('what yout age?'))
    if age< 12:
        print("please pay $5.")
    elif age <=18:
        bill = 7
        print("please pay $7.")
    elif age >= 45 and age <= 55:
        print("everthing is going to be ok. have a ride on us")
    else:
        print("Please pay $12.")
        bill = 12
        wants_photo = input ("do you want a photo taken? y or N")
        if wants_photo == "y":
            bill = bill + 3
        
else:
    print("sorry you have to grow taller before you can ride")
    
