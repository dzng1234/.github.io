def intro():
  print ("Welcome to the Sport trivia game!")
  print ("Which sport would you like to play?")
  print ("Press f for Football, s for Soccer, and b for Basketball")
  levelselect= raw_input()
  if levelselect==("f"):
    footballtrivia()
  elif levelselect==("s"):
    soccertrivia()
  else:
    basketballtrivia()

def levelselect():
  print ("\nWhich category would you like to play next?")
  print ("Press f for football, s for soccor, and b for basketball")
  print ("Press e to end the game")
  levelselect= raw_input()
  if levelselect==("f"):
    arttrivia()
  elif levelselect==("s"):
    soccertrivia()
  elif levelselect==("b"):
        print ("Thank you for playing!")
  else:
    basketballtrivia()



def footballtrivia():
  print ("Welcome to the football category of the game!")
  aq1=("How many NFL teams has Los Angeles had in it history?")
  aq2=("In their career, who has caught the most touchdown passes from Tom Brady?")
  aq3=("Which of these is not a real penalty?")
  aq4=("What position did Troy Polumalu play?")
  aq5=("What is the average success rate ow two-point conversions?")

  options1= ("a. 1\nb. 2\nc. 3\nd. 4")
  options2= ("a. Rob Gronkowski\nb. Wes Welker\nc. Randy Moss\nd. Antonio Brown")
  options3= ("a. Neutral Zone Infraction\nb. Horse Collar Tackle\nc. Uneccesary Roughness\nd. Pulling the Guard")
  options4= ("a. Line Backer\nb. Strong Safety\nc. Tight End\nd. Running Back")
  options5= ("a. 14%\nb. 21%\nc. 34%\nd. 48%")
  score=0
  
  print (aq1)
  print (options1)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/1")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/1")
  
  
  print (aq2)
  print (options2)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="a":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/2")
  else:
    print("The correct answer is a")
    score=score+0
    print ("Your score is", score,"/2")

  print (aq3)
  print (options3)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="d":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/3")
  else:
    print("The correct answer is d")
    score=score+0
    print ("Your score is", score,"/3")

  print (aq4)
  print (options4)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/4")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/4")

  print (aq5)
  print (options5)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="d":
    print ("Correct!")
    score=score+1
    if (score==5):
      print ("Good job on a perfect 5/5!")
    else: 
      print("Your score is", score,"/5")
  else:
    print("The correct answer is d")
    score=score+0
    print ("Your final score is", score,"/5")  
  levelselect()



def soccertrivia():
  print ("Welcome to the soccer category of the game!")
  mq1=("Who won the Champions League last year?")
  mq2=("Which player has never played on FC Barcelona?")
  mq3=("Who scored the most goals in their career?")
  mq4=("Which player did not score in the final of the 2018 World Cup?")
  mq5=("What player had the most expensive transfer?")

  options1= ("a. Tottenhem\nb. Liverpool\nc. Manchester City\nd. FC Barcelona")
  options2= ("a. Ibrahamovic\nb. Neymar\nc. Ronaldo\nd. Ronaldhino")
  options3= ("a. Josef Bican\nb. Pele\nc. Ronaldo\nd. Messi")
  options4= ("a. Mabppe\nb. Modric\nc. Pogba\nd. Manduzkic")
  options5= ("a. Ronaldo\nb. Van Dijk\nc.Neymar\nd. Messi")
  score=0
  
  print (mq1)
  print (options1)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/1")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/1")
  
  
  print (mq2)
  print (options2)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/2")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/2")

  print (mq3)
  print (options3)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="a":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/3")
  else:
    print("The correct answer is a")
    score=score+0
    print ("Your score is", score,"/3")

  print (mq4)
  print (options4)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/4")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/4")

  print (mq5)
  print (options5)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    if (score==5):
      print ("Good job on a perfect 5/5!")
    else: 
      print("Your score is", score,"/5")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your final score is", score,"/5")  
  levelselect()



def basketballtrivia():
  print("This is the basketball trivia!")
  mq1=("What is the record for most regular season wins, set by the Golden State Warriors in 2016?")
  mq2=("How many times has Steph Curry dunked?")
  mq3=("What is depicted on the logo of the Golden State Warriors?")
  mq4=("Who was the shortest player to win MVP?")
  mq5=("What is the record for highest average scoring average set by a person during a single season?")

  options1= ("a. 50\nb. 82\nc. 73\nd. 69")
  options2= ("a. 5\nb. 15\nc. 20\nd. 25")
  options3= ("a. A basketball\nb. A city skyline\nc. A bridge\nd. A spearhead")
  options4= ("a. A Charles Barkley\nb. Spudd Webb\nc. Allen Iverson\nd. Steve Nash")
  options5= ("a. 40.4\nb.50.4\nc. 35.4\nd. 49.4")
  score=0
  
  print (mq1)
  print (options1)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/1")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/1")
  
  
  print (mq2)
  print (options2)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="d":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/2")
  else:
    print("The correct answer is d")
    score=score+0
    print ("Your score is", score,"/2")

  print (mq3)
  print (options3)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/3")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/3")

  print (mq4)
  print (options4)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/4")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/4")

  print (mq5)
  print (options5)
  response= raw_input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    if (score==5):
      print ("Good job on a perfect 5/5!")
    else: 
      print("Your score is", score,"/5")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your final score is", score,"/5")  
  levelselect()

  levelselect()






intro()
