#Ryan McVicker
#12/3/2018

#command line interface that automatically finds answers to parsed questions in document
# ex: python bookworm.py <filename>

import random
import sys
import time
import os
from colorama import Fore, Style, init
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






def write_to_file(text, filename=None):

    #algorithm for fake-typing

    #parse through the text
    if filename is None:
        #prompt user to enter file name
        filename = input("ENTER NAME FOR ANSWER FILE: ")
        #need to add more space here
    print("_" * 100)
    print("writing to file.....")
    if os.path.exists(filename):
        #prompt user to enter a new file name
        print("appending to end of file.....")

        """ PARSE THROUGH DICT HERE NOT STR """


        with open(filename, 'a') as write_file:
            write_file.write(text)


    else:

        print("creating new file %s" % filename)
        with open(filename, 'w') as write_file:
            write_file.write(text)



#what is this method used for ?
def parse_directory_file(directory):
    #split list to get filename at end of dir string
    filename = directory.split('\t')[-1]
    #check to make sure file is text file
    if not filename.endswith('.txt'):
         return "Error: file needs to be text file"
           #ADD EXCEPTION HERE!!
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



def search_questions(array_of_questions):
    q_and_a = {}
    for question in array_of_questions:
        #list comprehension of urls found from google search
        list_of_urls = [url for url in search(question, num=10)]


        try:

            _url = random.choice(list_of_urls)

            _soup = BeautifulSoup(urlopen(_url))

            IS_VALID_URL = True

            for script in _soup(["script", "style"]):

                script.decompose()

            #get text from soup

            _text = _soup.get_text()
            shorten_text(_text, char=80) #PROPOSED METHOD

            #returns the text
            return _text

        except Exception as e:
            print("line 138: %s" % e)



