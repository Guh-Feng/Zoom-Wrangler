from WebScrape import Scraper
from ReadWriteCSV import Database
from tkinter import *

def main():
    #Test Sites
    #https://ufl.instructure.com/courses/447867/assignments/syllabus
    #https://ufl.instructure.com/courses/447867/pages/pm-slash-information?module_item_id=9127714
    #https://ufl.instructure.com/courses/447867
    #https://ufl.instructure.com/courses/447867/modules

    inValue = ''
    cyclesIn = 0

    #web scraping input
    def con():
        inValue = site.get(1.0, "end-1c")
        cyclesIn = cycle.get(1.0, "end-1c")
        top.destroy()

    top = Tk()
    top.geometry("300x100")
    top.title("Starting Site")
    
    site = Text(top, height = 2, width = 40)
    site.insert(INSERT, "<starting link>")
    site.pack()

    cycle = Text(top, height = 1, width = 40)
    cycle.insert(INSERT, "<number of cycles>")
    cycle.pack()

    conButton = Button(top, text = "Continue", command = con)
    conButton.pack()

    top.mainloop()

    """
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
    """

    webScraper = Scraper(inValue, cyclesIn)
    webScraper.scrapeWeb()
    
    zoom_links = webScraper.returnLinks()

    #new file input
    newness = True
    
    def yes():
        newness = True
        top2.destroy()

    def no():
        newness = False
        top2.destroy()

    top2 = Tk()
    top2.geometry("200x100")
    top2.title("New File?")
    
    txt = Text(top2, height = 2, width = 30)
    txt.insert(INSERT, "Are you starting a new file?")
    txt.pack()

    yesButton = Button(top2, text = "Yes", command = yes)
    yesButton.pack()

    noButton = Button(top2, text = "No", command = no)
    noButton.pack()

    top2.mainloop()
    

    
    """
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
    """
    
    db = Database(zoom_links, is_new = newness)
    
#    except Exception as exc:
#        print('There was a problem: %s' % (exc))

if __name__ == "__main__":
    main()
