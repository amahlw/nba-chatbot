

from random import choice

#combine functions and conditionals to get a response from the bot
def nba_finals_bot_response(user_response):

  #add some bot responses to this list
  bot_response_Lakers = ["Yesir!! KOBE", "Go Lakers!", "Aint nothing like purple an Gold!"]
  bot_response_Celtics = ["Sheesh i guess!", "Go Clover","Gang Green"]
  bot_response_Heat = ["305 to my city", "Wade County","Jimmy Buckets!!","Herro Ball"]
  bot_response_Nuggets = ["The Comeback Kidz","It's teh Joker","About Time👌"]

  if user_response.upper() ==  "LAKERS":
    return choice(bot_response_Lakers)
  elif user_response.upper() == "CELTICS":
    return choice(bot_response_Celtics)
  elif user_response.upper() == "HEAT":
    return choice(bot_response_Heat)
  elif user_response.upper() == "NUGGETS":
    return choice(bot_response_Nuggets)
  else:
    return "Better Luck Next Time😤"




print("Welcome to ya Finals Pick Bot")
# print("Who is your NBA Finals pick?")

user_response = ""

while True:
  user_response = input("Who is your NBA Finals pick? ")
  
  # Quits program when user responds with 'done'
  if user_response.upper() == 'HATE SPORTS':
    break

 

