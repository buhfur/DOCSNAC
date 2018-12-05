from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os



def main():
    question = "http error 503?"
    searchq = search(question, num=2)
    list_of_urls = [url for url in searchq]
    for url in list_of_urls:
        page_request = requests.get(url)
        html_doc = page_request.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        print(soup.get_text())
        print("________________________________________________________________")


if __name__ == '__main__':
    main()
