#Ryan McVicker


"""
script to modify a novel of text and find replacements for each word
using synonyms

- every api call will store the response json file and store the synonyms
    and the script should check for any
    json files in case the api isnt available

exmples:
    - the word "bite" could be replaced with the word
    - 

"""


import requests
import sys
import json
import os

def search_and_parse_json_file(word):
    #if the api isnt available, use stored json files
    return



def get_synonym(api_key, word):
    try:
        #couldent use %s for formatting
        url = "http://words.bighugelabs.com/api/2/{}/{}/json".format(api_key, word)
        #get the json from url
        response_json = url.json()
        #save the file
        with open('words.json', 'w') as json_file:



    except requests.exceptions.RequestException:
        print("requests couldent handle the url")


#take arguments from the command line
if __name__ == '__main__':
    """
    command :
        python docsnac.py [api_key] [word]
    """
    #verify if the url is legit
    get_synonym(sys.argv[1], sys.argv[2])
