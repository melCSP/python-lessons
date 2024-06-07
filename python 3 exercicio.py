print("welcome to the rollecuster")
height = int(input("what is yout heigth in cm?"))

if height >=120:
    print ("you can ride the rollercoaster")
    age = int(input('what yout age?'))
    if age< 12:
        print("please pay $5.")
    elif age <=18:
        print("please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("sorry you have to grow taller before you can ride")
    
