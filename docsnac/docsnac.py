#Ryan McVicker
#12/3/2018

#should be able to take raw text or a text file as input for any of these methods

import random
import sys
import time
import os
from googlesearch import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
#TODO: need to add more exceptions so testers can tell me what happened

def shorten_text(text,length=40):
    #encoding is set to utf as default
    text_list = text.split(' ')
    if len(text_list) > 40:
        text_list = text_list[:40]
    return ''.join(text_list)





""" this method takes in some text and possibly a filename. if there is no filename,
it prompts the user to enter a name for the file. after the user picks a name it checks
if the file exists on the disk, if it does, it appends the text to the end of the File.
If the file doesnt exist it creates the file on the disk and then immediately writes the text
to the file.

"""
def write_to_file(text, filename=None):


    #parse through the text
    if filename is None:
        #prompt user to enter file name
        filename = input("ENTER NAME FOR ANSWER FILE: ")
    print("_" * 100)

    print("writing to file.....")
    #checks if the file exists
    if os.path.exists(filename):
        print("appending to end of file.....")


        with open(filename, 'a') as write_file:
            write_file.write(text)


    else:

        print("creating new file %s" % filename)
        with open(filename, 'w') as write_file:
            write_file.write(text)





"""this method takes in a dir and then looks for a file, then checks if its a text file,
then looks for a lines with a '?' at the end of it. if it does have said character, then
it adds it to an array, and then returns it
"""
def parse_directory_file(directory):
    #split list to get filename at end of dir string
    filename = directory.split('\t')[-1]
    #check to make sure file is text file
    if not filename.endswith('.txt'):

         return "Error: file needs to be text file"

    else:

        print("-" * 43)
        #open the file for reading
        with open(filename, 'r') as read_file:
            print("parsing %s for questions...." % filename)
            #list comprehension for all questions and adds them to an array
            list_of_questions = [line_in_file for line_in_file in read_file.read().split('\n')
                                    if line_in_file.endswith("?")]
            #returns the list of questions
            return list_of_questions

"""this method takes in an array of questions to search online using google.
it begins by parsing the array_of_questions thus creating a list comprehension of
urls found on google related to the question. afterward it randomly selects a url from the
list 'list_of_urls' in order to search for text, as well as creating a soup object with
the returned text from the google search. after obtaining some text, it parses through the soup
object, decomposing and 
"""

def search_questions(array_of_questions):
    q_and_a = {}
    for question in array_of_questions:
        #list comprehension of urls found from google search
        list_of_urls = [url for url in search(question, num=10)]


        try:

            _url = random.choice(list_of_urls)

            _soup = BeautifulSoup(urlopen(_url))

            for script in _soup(["script", "style"]):

                script.decompose()

            #get text from soup

            _text = _soup.get_text()
            shorten_text(_text, char=80) #PROPOSED METHOD

            #returns the text
            return _text

        except Exception as e:
            print("line 138: %s" % e)



