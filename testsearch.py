from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
from docsnac import SearchQuestions

def main():
    question = "how to tie a tie?"
    searchq = search(question, num=10)
    list_of_urls = [url for url in searchq]
    for url in list_of_urls:
        page_request = requests.get(url)
        html_doc = page_request.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        for js_text in soup(["script","style"]):
            soup.decompose() #rips out javascript and css

        text = soup.get_text()
        print(text.encode('utf-8'))
        print("________________________________________________________________")




def sub(url):

    #COPIED FROM : https://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)


def test_text_file(filename):
    try:
        from docsnac import TextFile

    except ImportError:
        print("couldent load module")

    textFileObj = TextFile(filename)
    print(textFileObj.get_file_name())


def test_answer_dict():

    question_file = "C:\tDOCSNAC\tfirst.txt"
    array_of_questions = SearchQuestions.parse_directory_file(question_file)
    question_dict = SearchQuestions.search_questions(array_of_questions)
    #how to parse dict? cleanly
    for key in question_dict:
        print(key)



    #SearchQuestions.write_to_file(question_dict, filename=None)


if __name__ == '__main__':
    #main()

    #filename = "C:\tDOCSNAC\texample.txt"
    #test_text_file(filename)
