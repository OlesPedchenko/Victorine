score = 0
print("             Victorine")
print("""Which city is a capital of Ukraine?
a - Kyiv
b - Vienna
c - Moscow
""")
question1 = input()
if question1 == "a":
  print("Correct!!!")
elif question1 == "b":
  print("No, Vienna is a capital of Austria")
elif question1 == "c":
  print("Wrong, Mpscow is a capital of Russia" )
else:
  print("You choosed not offered version")
if question1 == "a":
  score = (score + 1) 

print(""" """)

print("""Where is a city of Monreal?
a - China
b - Egypt
c - Canada
""")
question2 = input()
if question2 == "a":
  print("It's wrong answer, try again")
elif question2 == "b":
  print("Nope, try another chance")
elif question2 == "c":
  print("You're right!" )
else:
  print("You choosed not offered version") 
if question2 == "c":
  score = (score + 1)

print(""" """)

print("""What country is on African continent?
a - USA
b - Sudan
c - Peru
""")
question3 = input()
if question3 == "a":
  print("USA is in North America, you are incorrect")
elif question3 == "b":
  print("It's a true answer!")
elif question3 == "c":
  print("Try again, Peru is in South America" )
else:
  print("You choosed not offered version")  
if question3 == "b":
  score = (score + 1)

print(""" """)

print("Your score is",score)
if score == 3:
  print("It's incredible, you know everything!")
elif score == 1:
  print("Good result!!!")
elif score == 2:
  print("Good result!!!")  
else:
  print("Try again, you can give correct answers!")