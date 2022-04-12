from WebScrape import Scraper
from ReadWriteCSV import Database

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
        userIn = input('\nIs this the correct website? (Y/N)\n')
        if userIn.capitalize() == 'Y':
            break
        elif userIn.capitalize() == 'N':
            continue
        else:
            continue

    webScraper = Scraper(inValue)
    webScraper.scrapeWeb()
    
    zoom_links = webScraper.returnLinks()
    
    while True:
        newness = input('\nWill you be creating a new file? (Y/N)\n')
        if newness.capitalize() == 'Y':
            newness = True
            break
        elif newness.capitalize() == 'N':
            newness = False
            break
        else:
            print('Invalid input!')
            continue
    
    db = Database(zoom_links, is_new = newness)
    
#    except Exception as exc:
#        print('There was a problem: %s' % (exc))

if __name__ == "__main__":
    main()