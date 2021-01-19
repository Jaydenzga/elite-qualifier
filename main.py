import random

UserInput = "Typer"
ChatBot_Name = "Ace"
print(": Hey there")
UserInput = str.lower(input(": "))
ignore_words = ["!", "?", "'"]
if UserInput == ["who are you?","Hi","Whats up","who made you"]:
 print(ChatBot_Name + ": My name is Ace, I am a chatbox created by Jayden Banks") 
if UserInput == "how are you?":
 print(ChatBot_Name + ": Im doing great")

def generate_response(user_input):
  responses = [
    "oooo nice",
    "You don't say!",
    "Very cool!",
    "I like that"
  ]
  return random.choice(responses)

def init_chat():
  Chatbot_Name = 'Ace'
  quit_character = 'q'

  user_input = input( Chatbot_Name + ": how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()