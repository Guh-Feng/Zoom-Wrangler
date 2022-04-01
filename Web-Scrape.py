from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlparse, urljoin
import bs4
import re
import time

#Functions
#Finds all links in HTML
#One for internal links and one for zoom links

#Filters list of links for zoom links
class Scraper:
    def __init__(self):
        self.crawlSites = {}
        self.zoomLinks = []
        self.site = ""

    #Check for valid link
    def is_valid(self, link):
        parsed = urlparse(link)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def extractLinks(self, html):
        parse = bs4.BeautifulSoup(html, 'lxml')
        for link in parse.find_all('a', href = True):
            #If it is an external link, it is placed into a list to filter for zoom links
            url = urlparse(link.get('href'))
            if(url.scheme == 'https' and bool(url.netloc)):
                self.zoomLinks.append(link.get('href'))
            #If it is an internal link, it is placed into the dictionary for crawling
            elif(url.scheme != 'mailto' and bool(url.path) and not bool(url.fragment)):
                self.crawlSites[urljoin(self.site, urlparse(link.get('href')).path)] = False

    #Filters zoom links list to keep zoom links
    def zoomProcess(self):
        linkRegex = re.compile(r'ufl.zoom.us')
        iterator = 0
        listLen = len(self.zoomLinks)
        while iterator < listLen:
            zoomFind = linkRegex.search(self.zoomLinks[iterator])
            if(zoomFind):
                if(zoomFind.group() == 'ufl.zoom.us'):
                    iterator = iterator + 1
                    continue
            else:
                self.zoomLinks.remove(self.zoomLinks[iterator])
                listLen = len(self.zoomLinks)
        self.zoomLinks = list(set(self.zoomLinks))

    def printZoom(self):
        for links in self.zoomLinks:
            print(links)
            print('\n')

    #Inputs links into the dictionary, make sure they are valid and filtered links
    def linksDictionary(self, links):
        for link in links:
            if link not in self.crawlSites:
                self.crawlSites[link] = False

def main():
    #CEN Syllabus Webpage
    #https://ufl.instructure.com/courses/447867/assignments/syllabus
    #https://ufl.instructure.com/courses/447867/pages/pm-slash-information?module_item_id=9127714
    #https://ufl.instructure.com/courses/447867

    inValue = ''
    webScraper = Scraper()
    while True:
        inValue = input('Enter website:')

        userIn = input('\nIs this the correct website? Y/N\n')
        if userIn == 'Y':
            break
        elif userIn == 'N':
            continue
        else:
            continue

    try:
        browser = webdriver.Firefox()
        browser.get(inValue)
        webScraper.site = inValue
        while True:
            userIn = input('\nHave you logged in?\n')
            if userIn == 'Y':
                html = browser.page_source
                webScraper.extractLinks(html)
                webScraper.zoomProcess()
                webScraper.printZoom()
                break
            else:
                continue
    except Exception as exc:
        print('There was a problem: %s' % (exc))

if __name__ == "__main__":
    main()


            

#User navigates page and program gives option to scan the open page
#Checks through pages, modules, and Zoom conferences tabs
#Double hashtables via dictionaries, one for checked sites and one for unchecked sites for crawling pages
#saveFile = open('site.txt', 'wb')