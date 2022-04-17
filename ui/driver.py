from WebScrape import Scraper
from ReadWriteCSV import Database
from tkinter import *

def main():
    #Test Sites
    #https://ufl.instructure.com/courses/447867/assignments/syllabus
    #https://ufl.instructure.com/courses/447867/pages/pm-slash-information?module_item_id=9127714
    #https://ufl.instructure.com/courses/447867
    #https://ufl.instructure.com/courses/447867/modules
    
    #web scraping input
    def con():
        global inValue, cyclesIn
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

    global inValue, cyclesIn
    webScraper = Scraper(inValue, cyclesIn)
    webScraper.scrapeWeb()
    
    zoom_links = webScraper.returnLinks()

    #new file input
    def yes():
        global newness
        newness = True
        top2.destroy()

    def no():
        global newness
        newness = False
        top2.destroy()

    top2 = Tk()
    top2.geometry("300x100")
    top2.title("New File?")
    
    global file_name

    txt = Text(top2, height = 2, width = 30)
    txt.insert(INSERT, "Are you starting a new file?")
    txt.pack()

    yesButton = Button(top2, text = "Yes", command = yes)
    yesButton.pack()

    noButton = Button(top2, text = "No", command = no)
    noButton.pack()

    top2.mainloop()

    top3 = Tk()
    top3.geometry("300x100")
    top3.title("File name?")

    fn = Text(top3, height = 2, width = 30)
    fn.insert(INSERT, "<file name>")
    fn.pack()
    
    def con2():
        global file_name_
        file_name_ = fn.get(1.0, "end-1c")
        top3.destroy()

    conButton2 = Button(top3, text = "Continue", command = con2)
    conButton2.pack()

    top3.mainloop()


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
    
    global newness
    db = Database(zoom_links, is_new = newness, file_name = file_name_)
    
#    except Exception as exc:
#        print('There was a problem: %s' % (exc))

if __name__ == "__main__":
    main()
