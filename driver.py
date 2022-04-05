from WebScrape import Scraper
import csv
import time
import webbrowser
from datetime import datetime, date, timedelta

def main():
    #Test Sites
    #https://ufl.instructure.com/courses/447867/assignments/syllabus
    #https://ufl.instructure.com/courses/447867/pages/pm-slash-information?module_item_id=9127714
    #https://ufl.instructure.com/courses/447867
    #https://ufl.instructure.com/courses/447867/modules

    inValue = ''

#    try:
    while True:
        inValue = input('Enter website: ')
        userIn = input('\nIs this the correct website? Y/N\n')
        # TODO: Add support for lower-case Y/N and a message that
        # tells the user that the input is invalid if not Y/N
        if userIn == 'Y':
            break
        elif userIn == 'N':
            continue
        else:
            continue

    webScraper = Scraper(inValue)
    webScraper.scrapeWeb()
    
    zoomLinks = webScraper.returnLinks()
    
    
#    except Exception as exc:
#        print('There was a problem: %s' % (exc))

if __name__ == "__main__":
    main()