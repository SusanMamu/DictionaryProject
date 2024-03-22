import json
from difflib import get_close_matches

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_definition(word, dictionary):
    word = word.lower() 
    if word in dictionary:
        return dictionary[word]
    
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        closest_match = get_close_matches(word, dictionary.keys())[0]
        suggestion = input(f"Did you mean '{closest_match}' instead of '{word}'? Enter 'yes' or 'no': ").lower()
        if suggestion == 'yes':
            return dictionary[closest_match]
        else:
            return "Word not found in dictionary."
    
    else:
        return "Word not found in dictionary."

# Load dictionary data
dictionary_data = load_dictionary('data.json')

word = input("Enter a word to search for its definition: ")
definition = get_definition(word, dictionary_data)
print(definition)
