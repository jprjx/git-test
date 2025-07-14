#level 1
import os
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
name = input("what is your name? ")
total = 0
tries = 0

clear_screen()

q = input("hello "+name+" how many questions do you want? (max 10) ")

while int(q) > 10:
  q = input("\nPlease enter a number less than 10. ")
  if int(q) <= 10: 
    break

clear_screen()

print("\nWelcome to the adding game "+name+"!")
start = input("\nPress enter to start the game.")

clear_screen()
print("Level 1")
print("\nRules of Level 1")
print("\nYou will add two numbers between 0 and 10.")
print("\n\n +1 point for each correct answer.")
print("\n -1 points per incorrect answer.")
print("\nYou need "+q+" point(s) to finish the game.")
print("\nGood luck "+name+"!")
num = input("\nPress enter to start the game.")
clear_screen()

while total < int(q):
  a = random.randint(0,10)
  b = random.randint(0,10)
  print("\nWhat is the sum of ", str(a),"and",str(b)+"?")
  ans = int(input(""))
  if ans == a+b:
    tries = tries+1
    total = total + 1
    print("\nYou are correct. You have",total,"points in total!")
  if total > 0:
    if ans != a+b:
      tries = tries + 1
      total = total - 1
      if total > 1:
        print("You are NOT correct. You still have",total,"points in total!")  
      if total <= 1 or total <= 0:
        print("You are NOT correct. You still have",total,"point in total!")
  elif total == 0:
    print("you still have",total,"in total.")
  if total == int(q):
    print("\nCongragulations "+name+" You have finished the adding game.")
    print("\n\nYour percentage is:",float(round(total/tries*100,2)),"%")
    t = input("\nPress enter to clear screen.")
clear_screen()

#level 2
print("Congradulations "+name+" you have finished level 2.")
print("\n\nYou have now unlocked our bonus level 2. Advanced Addition!!")
h2 = input("\n\nPress Y to start level 2. or press N to stop the game.")
if h2 == "y":
  clear_screen()
if h2 != "y":
  clear_screen()
  print("Thank you for playing the game.")
  exit()  #this will stop the game

num = input("\nPress enter to start the game.")
clear_screen()

trys = 0
points = 0

print("Level 2")
print("\nRules of Level 2")
print("\nYou will add two numbers between 0 and 19.")
print("\n\n +1 point for each correct answer.")
print("\n -1 points per incorrect answer.")
print("\nYou need "+str(points)+" point(s) to finish the game.")
print("\nGood luck "+name+"!")
num = input("\nPress enter to start the game.")
clear_screen()

while points < 8: 
  ask1 = random.randint(0,19)
  ask2 = random.randint(0,19)
  print("\nWhat is the sum of ", str(ask1),"and",str(ask2)+"?")
  answer = int(input(""))
  if answer == ask1+ask2:
    trys = trys+1
    points = points + 1
    print("You are correct. You have",points,"points in points!")
  if points > 0:
    if answer != ask1+ask2:
      trys = trys + 1
      points = points - 2
      print("You are NOT correct. You still have",points,"points in points!")
  elif points == 0:
    print("you still have",points,"in points.")
  if points == 8:
    print("\ncongragulations "+name+" You have finished the adding game.")
    print("\nYour percentage is:",float(round(points/trys*100,2)),"%")
    z = input("\nPress enter to clear screen.")
    clear_screen()

#level 3
print("Congradulations "+name+" you have finished level 2.")
print("\nYou have now unlocked our bonus level 3. Multiplication!!")
h = input("\n\nPress Y to start level 3. or press N to stop the game.")
if h == "y":
  clear_screen()
if h != "y":
  clear_screen()
  print("Thank you for playing the game.")
  exit() #this will stop the game
  
num = input("\nPress enter to start the game.")
clear_screen()

tr = 0
po = 0

print("Level 3")
print("\nRules of Level 3")
print("\n")
print("You will multiply two numbers between 0 and 9.")
print("\n\n +1 point for each correct answer.")
print("\n -1 points per incorrect answer.")
print("\nYou need "+str(po)+" point(s) to finish the game.")
print("\nGood luck "+name+"!")
num = input("\nPress enter to start the game.")
clear_screen()

while po < 6: 
  ask1 = random.randint(0,9)
  ask2 = random.randint(0,9)
  print("\nWhat is the multiple of ", str(ask1),"*",str(ask2)+"?")
  answer = int(input(""))
  if answer == ask1*ask2:
    tr = tr+1
    po = po + 1
    print("You are correct. You have",po,"points in points!")
  if po > 0:
    if answer != ask1*ask2:
      tr = tr + 1
      po = po - 1
      print("You are NOT correct. You still have",po,"points in points!")
  elif po == 0:
    print("you still have",po,"in points.")
  if po == 6:
    print("\ncongragulations "+name+" You have finished the adding game.")
    print("\nYour percentage is:",float(round(po/tr*100,2)),"%")
    z = input("\nPress enter to clear screen.")
    clear_screen()