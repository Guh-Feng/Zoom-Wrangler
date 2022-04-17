from WebScrape import Scraper
from ReadWriteCSV import Database

def print_menu():
    print('1. Crawl from a starting page and create/add to database')
    print('2. Read from a given database')
    print('3. Load UI from given database')
    print('0. Quit')

def main():
    #Test Sites
    #https://ufl.instructure.com/courses/447867/assignments/syllabus
    #https://ufl.instructure.com/courses/447867/pages/pm-slash-information?module_item_id=9127714
    #https://ufl.instructure.com/courses/447867
    #https://ufl.instructure.com/courses/447867/modules

    inValue = ''
    cyclesIn = 0
    menu_choice = -1
    db = []
    while menu_choice != 0:
        print_menu()
        menu_choice = input('What would you like to do? ')
        if menu_choice == '1':
            while True:
                inValue = input('Enter website: ')
                userIn = input('\nIs this the correct website? (Y/N)\n')
                if userIn.capitalize() == 'Y':
                    cyclesIn = input('\nHow many pages do you want to search? Type 0 to search all available pages.\n')
                    break
                elif userIn.capitalize() == 'N':
                    continue
                else:
                    continue

            webScraper = Scraper(inValue, cyclesIn)
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

            if newness:
                print('Created new file named', db.file_name, 'and added', db.num_entries(), 'entries')
            else:
                print('Added', db.diff_entries(), 'entries', 'to', db.file_name)
        elif menu_choice == '2':
            zoom_links = []
            db = Database(zoom_links, is_new = False)
        elif menu_choice == '3':
            zoom_links = []
            db = Database(zoom_links, is_new = False)
    
    
if __name__ == "__main__":
    main()