from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlparse, urljoin
import bs4
import re
import time

#Primary class
class Scraper:
    def __init__(self, starterSite, starterCycles):
        self.crawlSites = {}
        self.zoomLinks = []
        self.site = starterSite
        # TODO: Add options for which browser to use.
        #self.browser = webdriver.Firefox()
        #self.browser = webdriver.Safari()
        self.browser = webdriver.Chrome()
        self.cycles = int(starterCycles)

    #Finds and filters links
    def extractLinks(self, html):
        parse = bs4.BeautifulSoup(html, 'lxml')
        #Processes extracted links
        for link in parse.find_all('a', href = True, download = False):
            #If it is an external link, it is placed into a list to filter for zoom links
            url = urlparse(link.get('href'))
            if(url.scheme == 'https' and bool(url.netloc)):
                self.zoomLinks.append(link.get('href'))
            #If it is an internal link, it is placed into the dictionary for crawling
            elif(url.scheme != 'mailto' and bool(url.path) and not bool(url.fragment)):
                if(urljoin(self.site, urlparse(link.get('href')).path) not in self.crawlSites):
                    self.crawlSites[urljoin(self.site, urlparse(link.get('href')).path)] = False

    #Filters out external links to keep Zoom links
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

    #Prints Zoom list
    def printZoom(self):
        for links in self.zoomLinks:
            print(links)
            print('\n')

    #Scrapes Canvas from a starting link
    def scrapeWeb(self):
        self.browser.get(self.site)
        while True:
            userIn = input('\nHave you logged in? (Y/N)\n')
            if userIn.capitalize() == 'Y':
                break
            elif userIn.capitalize() == 'N':
                continue
        html = self.browser.page_source
        
        print('\nProcessing links.')
        self.extractLinks(html)
        self.zoomProcess()

        #If cycles is 0, it scrapes for as long as possible, otherwise, it scrapes for amount of pages provided by user
        if(self.cycles):
            for i in range(self.cycles):
                try:
                    crawlIter = iter(self.crawlSites)
                    crawlSite = next(crawlIter) 
                    while self.crawlSites[crawlSite] == True:
                        crawlSite = next(crawlIter)
                    self.browser.get(crawlSite)
                    self.crawlSites[crawlSite] = True
                    html = self.browser.page_source
                    self.extractLinks(html)
                    self.zoomProcess()
                except StopIteration:
                    break
        else:
            while True:
                try:
                    crawlIter = iter(self.crawlSites)
                    crawlSite = next(crawlIter) 
                    while self.crawlSites[crawlSite] == True:
                        crawlSite = next(crawlIter)
                    self.browser.get(crawlSite)
                    self.crawlSites[crawlSite] = True
                    html = self.browser.page_source
                    self.extractLinks(html)
                    self.zoomProcess()
                except StopIteration:
                    break

    #Inputs links into the dictionary, make sure they are valid and filtered links
    def linksDictionary(self, links):
        for link in links:
            if link not in self.crawlSites:
                self.crawlSites[link] = False
                
    def returnLinks(self):
        return self.zoomLinks


#User navigates page and program gives option to scan the open page
#Checks through pages, modules, and Zoom conferences tabs
#Double hashtables via dictionaries, one for checked sites and one for unchecked sites for crawling pages
#saveFile = open('site.txt', 'wb')
        #self.printZoom()
        