#Ryan McVicker
#12/3/2018

#command line interface that automatically finds answers to parsed questions in document
# ex: python bookworm.py <filename>

second_text = """
v1.1--

▓█████▄  ▒█████   ▄████▄    ██████  ███▄    █  ▄▄▄       ▄████▄
▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█  ▒██    ▒  ██ ▀█   █ ▒████▄    ▒██▀ ▀█
░██   █▌▒██░  ██▒▒▓█    ▄ ░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▒▓█    ▄
░▓█▄   ▌▒██   ██░▒▓▓▄ ▄██▒  ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒
░▒████▓ ░ ████▓▒░▒ ▓███▀ ░▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒ ▓███▀ ░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░
 ░ ▒  ▒   ░ ▒ ▒░   ░  ▒   ░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░  ▒
 ░ ░  ░ ░ ░ ░ ▒  ░        ░  ░  ░     ░   ░ ░   ░   ▒   ░
   ░        ░ ░  ░ ░            ░           ░       ░  ░░ ░
 ░               ░                                      ░

________________________________________________________________________________
This is docsnac your tool for auto completing your
assignments
________________________________________________________________________________
Made by : Ryan McVicker
________________________________________________________________________________
Date : 12/3/2018
________________________________________________________________________________
Please use this software as a means of auto-completing your assignments |
________________________________________________________________________________
TYPE QUIT TO END APPLICATION

-Please enter the directory of your text file that has all the questions.
 _________________________________________
|       WHAT DOES THIS PROGRAM DO????    |
-----------------------------------------
|   1. finds the predicted answer to your questions on a text file
|   2. uses an algorithm to enter the characters as if you are the one who typed it
|   3. saves the anwers to a text document which you can then upload to google classroom
________________________________________________________________________________



"""
import random
import sys
import time
import os
from colorama import Fore, Style, init
from googlesearch import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
#TODO: need to add more exceptions so testers can tell me what happened


class SearchQuestions:

    @staticmethod
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



    """
    return : <returns list of questions parsed from file>
    """
    @staticmethod
    def parse_directory_file(directory):
        #split list to get filename at end of dir string
        filename = directory.split('\t')[-1]
        #check to make sure file is text file
        if not filename.endswith('.txt'):
            return "Error: file needs to be text file"
            #ADD EXCEPTION HERE!!
        else:
            #line to keep things clean
            print("-" * 43)
            #open the file for reading
            with open(filename, 'r') as read_file:
                print("parsing %s for questions...." % filename)
                #list comprehension for all questions and adds them to an array
                list_of_questions = [line_in_file for line_in_file in read_file.read().split('\n')
                                    if line_in_file.endswith("?")]

                return list_of_questions


    """ <return> : returns a dictionary of [question:answer] form """
    @staticmethod
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



                return q_and_a

            except Exception as e:
                print("line 138: %s" % e)










if __name__ == '__main__':

    print(second_text)
    #init() filters out any ANSI codes, thus starting colorama
    init()
    print(Fore.RED + ' \t\tWARNING:\n \ti am not responsible for any misuse of this program be it through\n \tplagiarism or any other abuse')
    #restore stdin to its normal state, diabling colorama
    print(Style.RESET_ALL)
    while True:

        question_file = input("""
        \n\n
        _______________________
        | ENTER DIR NAME HERE | :  """)

        if question_file == "quit":
            #end the program
            sys.exit()

        while not os.path.exists(question_file):

            question_file = input("""
            \n\n
            _______________________
            | ENTER DIR NAME HERE | :  """)


        try:


            array_of_questions = SearchQuestions.parse_directory_file(question_file)
            question_dict = SearchQuestions.search_questions(array_of_questions)
            SearchQuestions.write_to_file(question_dict, filename=None)

        except Exception as e:
            print(e)
