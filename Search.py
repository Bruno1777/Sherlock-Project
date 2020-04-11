import requests
import nltk
from bs4 import BeautifulSoup
from grammarbot import GrammarBotClient

CREDIBLE_DOMAINS = ['gov', 'edu', 'int', 'mil']


class Search:
    def __init__(self, website):
        self.website = website

    def getWebsite(self):
        return self.website

    def isValid(self):
        response = requests.get(self.website)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            return False

    def isCredible(self, credibleFile, nonCredibleFile):
        nameList = self.website.split('/')
        if nameList[0] == "http:" or nameList[0] == "https:":
            name = nameList[2]
        else:
            name = nameList[0]
        name = name + "\n"
        credibleList = self.fileList(credibleFile)
        nonCredibleList = self.fileList(nonCredibleFile)
        if name in credibleList:
            return True
        elif name in nonCredibleList:
            return False
        else:
            credibility = self.chekingCredibilitiy()
            return credibility

    def fileList(self, file):
        credibleList = []
        file = open(file, 'r')
        data = file.readlines()
        for line in data:
            credibleList.append(line)
        return credibleList

    def getText(self):
        textList = []
        html_content = requests.get("https://www.bbc.com/news/world-us-canada-52241221").text
        soup = BeautifulSoup(html_content, 'html')
        for i in soup.findAll('p'):
            textList.append(i.text)
        text = ' '.join(textList)
        return text

    def chekingCredibilitiy(self):
        domain = ""
        nameList = self.website.split('.')
        if nameList[0] == "www":
            domain = nameList[2]
        else:
            domain = nameList[1]
        if domain.lower() in CREDIBLE_DOMAINS:
            return True
        else:
            client = GrammarBotClient()
            text = self.getText()
            errors = client.check(text, "en-US")
            if len(errors.matches) < 4:
                return False
            else:
                return True
