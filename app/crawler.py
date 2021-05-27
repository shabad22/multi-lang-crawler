import logging
from os import link
from bs4 import BeautifulSoup
import requests
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Crawl():
    def __init__(self, link = link):
        self.link = link
        self.fetched_data = requests.get(link)
        self.soup = BeautifulSoup(self.fetched_data.content, 'html.parser')
    
    def fetch_links(self):
        tempSublinks = [sublink['href'] for sublink in self.soup.find_all('a', href=True)]
        self.sublinks = []
        for sublink in tempSublinks:
            if str(sublink).startswith('http') == False:
                sublink = str(self.link)+str(sublink)
            self.sublinks.append(sublink)
        return set(self.sublinks)
    
    def crawl_data(self):
        self.globaltext = ''
        for sublink in set(self.sublinks):
            htmlcontent = requests.get(sublink)
            soup = BeautifulSoup(htmlcontent.content, 'html.parser')
            tags = list(set([tag.name for tag in soup.find_all()]))
            for tag in tags:
                for inf in soup.find_all(tag):
                    self.globaltext += inf.text + "%@%"
            return self.globaltext

                    