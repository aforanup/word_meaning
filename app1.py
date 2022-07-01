import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def meaning(word):
    close_word = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif len(close_word) > 0:
        yn = input(f"did you meant to type {close_word[0]}?? y/n : ")
        if yn == "y":
            return data[close_word[0]]
        elif yn=="n":
            return "sorry no such word found"
        else:
            return "couldnot understand your entry"
    else:
        return "sorry no such word found"

word=input("Enter a word : ").lower()

translated = meaning(word)

if type(translated) == list:
    for each in translated:
        print(each)
else:
    print(translated)



