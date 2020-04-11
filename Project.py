import articleDateExtractor
from bs4 import BeautifulSoup
import requests
def main():
    text = []
    html_content = requests.get("https://www.bbc.com/news/world-us-canada-52241221").text
    soup = BeautifulSoup(html_content, 'html')
    for i in soup.findAll('p'):
       print(i.text)
       text.append(i.text)
    lol = ' '.join(text)
    print(lol)




main()