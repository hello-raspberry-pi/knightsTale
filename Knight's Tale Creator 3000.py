# Title: Knight's Tale Creator 3000
# Author: Zachary Theilen
# This is an interactive game that knight's tales
# based on input from the user

# Display a welcome message
greeting = "Well met, heroic adventurer! Let us share your tale!"
print("*" +"*" * len(greeting) + "*")
print("*" + greeting + "*")
print("*" +"*" * len(greeting) + "*")

# Get the user's name and say hi
player_name = input("What be thy name? ")
message = "Yes, " + player_name + "! Let us recall your glory!"
print(message)

# Gather words from the player for our sentences
person_in_room = input("First, I'll need the name of someone in the room... ")
adjective = input("Yes, of course. Next I'll need an adjective... ")
animal = input("Hmm? Strange! But it's your story... Ok, an animal please... ")
vacation_place = input("My favorite! Now, your favorite place to vacation? ")
sharp_thing = input("Ah. Never been there. Now tell me something that's sharp. ")
exclamation = input("And what do you shout when you're very happy or angry? ")

# Create the story by joining together the words
story = ("There was a brave knight, " + player_name + ", who was sent on a " +
         "quest to vanquish the " + adjective + " evildoer, " + person_in_room +
         ". Riding on his/her trusty " + animal + ", the brave " + player_name +
         " traveled to the faraway land of " + vacation_place + ". " +
         player_name + " battled valiantly against " + person_in_room +
         "'s army using his/her " + sharp_thing + " until he/she defeated them. " +
         "Emerging victorious, " + player_name + " exclaimed, '" + exclamation +
         "!!!' I claim the land of " + vacation_place + " in the name of Python.")

# Display the story to the screen
print("*" * 79)
print(story)
print("*" * 79)
