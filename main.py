score = 0
print("Welcome to the joke machine!")
print("Guess the punchline...")
print("What is pink and fluffy?")
pink = input().lower()
if pink == "pink fluff":
  print("You got it!")
  score = score + 1
else:
  print("Incorrect. The answer was pink fluff.")
print("What is brown and sticky?")
brown = input().lower()
if brown == "a brown stick":
  print("You got it! One more!")
  score = score + 1
elif brown == "brown stick":
  print("You got it! One more!")
  score = score + 1
else:
  print("Incorrect. The answer was a brown stick.")
print("What is black and white and red all over?")
news = input().lower()
if news == "a newspaper":
  print("You got it! Well done!")
  score = score + 1
elif news == "newspaper":
  print("You got it! Well done!")
  score = score + 1
elif news == "a news paper":
  print("You got it! Well done!")
  score = score + 1
elif news == "news paper":
  print("You got it! Well done!")
  score = score + 1
else:
  print("Incorrect. The answer was a newspaper.")
if score == 3:
  print("You got 3 punchlines out of 3! Well done!")
elif score == 2:
  print("You got 2 punchlines out of 3. Nice try!")
elif score == 1:
  print("You only got 1 punchline out of 3. Try again to do better!")
elif score == 0:
  print("You didn't get any punchlines correct. Better luck next time!")