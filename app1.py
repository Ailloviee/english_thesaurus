import json
from difflib import SequenceMatcher


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return f'The word "{word}" doesn\'t exist. Please double check it.'


# load the json file into a dictionary object
data = json.load(open("data.json"))
# get user input which is the word
while True:
    word = input("Enter word: ")
    print(translate(word))
