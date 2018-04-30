import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes and n if no." % get_close_matches(w, data.keys()) [0])
        if yn == "y":
            return data[get_close_matches(w, data.keys()) [0]]
        elif yn == "n":
            return "I'm all out of ideas. Sorry!"
        else:
            yn2 = input("Sorry, dude. You have to enter y or n for me to understand. Enter y if you meant %s or n if you didn't." % get_close_matches(w, data.keys()) [0])
            if yn2 == "y":
                return data[get_close_matches(w, data.keys()) [0]]
            elif yn2 == "n":
                return "I'm all out of ideas. Sorry!"
            else:
                return "Help me... help you... That's still not the input I need." 
    else:
        return "That damn thing ain't a word!"

w = input("Enter word: ").lower()

output = translate(w)

if type(output) == list:
    for item in output:
        print(item)
else:
     print(output)