import json
from difflib import SequenceMatcher, get_close_matches


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    # if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:
        return data[word.title()]
    # in case user enters words like USA or NATO
    elif word.upper() in data:
        return data[word.upper()]
    # recommend the closest match to the input word based on the highest SequenceMatcher().ratio()
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_match = get_close_matches(word, data.keys())[0]
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: \n" % closest_match
        )
        if yn.lower() == "y":
            return data[closest_match]
        elif yn.lower() == "n":
            return f'The word "{word}" doesn\'t exist. Please double check it.'
        else:
            return "We didn't understand your entry."
    else:
        return f'The word "{word}" doesn\'t exist. Please double check it.'


# load the json file into a dictionary object
data = json.load(open("data.json"))
# get user input which is the word
while True:
    word = input("Enter word: ")
    output = translate(word)
    # if the output is a list of definitions, print them iteratively
    if type(output) == list:
        for index, item in enumerate(output):
            print("Definition %d: " % (index + 1) + item)
    else:
        print(output)
