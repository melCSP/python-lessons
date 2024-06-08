print ("the love calculator is calculating your score ....")
name1 = input ()
name2 = input ()

combined_names = name1 + name2
lower_names = combined_names.lower ()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count ("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count ("l")
o = lower_names.count ("o")
v = lower_names.count ("v")
e = lower_names.count ("e")
secound_digit = l + o + v + e

score = int (str (first_digit) + str(secound_digit))
if (score < 10 ) or (score > 99):
    print("your score is {score}, you together like coke and mentos")
elif (score >= 40 ) and (score <= 50):
    print ("your score is {score}, you are alight togueter")
else:
    print ("your score is {score}")


