from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os



def main():
    #method that searches for a question
    question = "http error 503?"
    searchq = search(question, num=2)
    list_of_urls = [url for url in searchq]
    for url in list_of_urls:
        page_request = requests.get(url)
        html_doc = page_request.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        print(soup.get_text())
        print("________________________________________________________________")
        
        
def sub(question):
    
    #search the question on google
    searchq = search(question, num=2)
    #create a list of urls returned from searchq
    list_of_urls = [url for url in searchq]
    #index the first url due to timeout restraint
    url = list_of_urls[0]
    #parse through soup([]) for the elements returned 
    for script in soup(["script","style"]):
        #delete the elements returned 
        script.decompose() 
     #get all text from the modified soup
    text = soup.get_text() 
    #what does this do????
    lines = (line.strip() for line in text.splitlines()
    #what does this do???
    chunks = (phrase.strip() for line in lines for phase in line.split("  "))
    print(text.encode('utf-8'))
    
    try:
             #check if file exists 
             
 
if __name__ == '__main__':
    main()
