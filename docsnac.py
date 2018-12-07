#Ryan McVicker
#12/3/2018

#command line interface that automatically finds answers to parsed questions in document
# ex: python bookworm.py <filename>

second_text = """
v1.4.18--

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

================================================================================
This is book worm. your tool for auto completing your
assignments

--------------------------------------------------------------------------------
Made by : Ryan McVicker

Date : 12/3/2018

________________________________________________________________________________



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Please use this software as a means of auto-completing your assignments |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


TYPE QUIT TO END APPLICATION

-Please enter the directory of your text file that has all the questions.






 _________________________________________
|       WHAT DOES THIS PROGRAM DO????    |
-----------------------------------------
|   1. finds the predicted answer to your questions on a text file
|   2. uses an algorithm to enter the characters as if you are the one who typed it
|   3. saves the anwers to a text document which you can then upload to google classroom
       (or type the answers found yourself to be safe :p)
________________________________________________________________________________
                WARNING:
            i am not responsible for any misuse of this program be it through
            plagiarism or any other abuse


 |------------------------------------------|
 |         LIST OF COMMANDS                 |
 |------------------------------------------|
 |  enter text file: <FILENAMEHERE>
 |  change default answer file: python mkfile.py <filename>
 |


"""


import time
import os
import sys
from googlesearch import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
#TODO: need to add more exceptions so testers can tell me what happened


class SearchQuestions:

    def write_to_file(self):
        #algorithm for fake-typing, creating the new file to be
        return
        
    """
    return : <returns list of questions parsed from file
    """
    def parse_file(self, dir):

        self.filename = dir.split('\t')[-1]

        #parse the file and look for questions
        if not self.filename.endswith('.txt'): #check to make sure file is text file
            return "Error: file needs to be text file"
            #ADD EXCEPTION HERE!!
        else:
            print("------------------------------------------------------")
            with open(self.filename, 'r') as read_file:
                file_data = read_file.read()
                list_of_questions = []
                print("parsing %s for questions...." % self.filename)

                for line_in_file in file_data.split('\n'):
                    if line_in_file.endswith("?"):
                        list_of_questions.append(line_in_file)
                self.search_questions(list_of_questions)

                return list_of_questions


    def search_questions(self, array_of_questions):
        #create separate file for questions and answers



        for question in array_of_questions:
            #search for answer here
            found_urls = search(question, num=10) #get 10 results
            #make get request to web page
            list_of_urls = [url for url in found_urls]

            #parse through list_of_urls and make get requests
            for url in list_of_urls:
                #download all text off of page
                _htmldoc = urlopen(url)
                _soup = BeautifulSoup(html_doc)

                #parse all the javascript out of the text
                for script in _soup(["script", "style"]):
                    script.decompose()

                 _text = soup.get_text()

                 lines = [line.strip() for line in _text.splitlines()]

                 chunk = [phrase.strip() for line in lines for phrase in line.split(' ')]
                 _text = '\n'.join(chunk for chunk in chunks if chunk)

                 #now write the question text to new  file unless stated other wise
                 self.write_to_file()










if __name__ == '__main__':

    print(second_text)
    while True:
        question_file = input("""
        =====================
        | ENTER DIR NAME HERE | : """)
        if user_input == "quit":
            break

        SearchQuestions.parse_file(question_file)
