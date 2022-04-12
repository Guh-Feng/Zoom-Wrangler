from tkinter import *
import csv

root = Tk()
root.title('Zoom Wrangler')
#root.iconbitmap('wrangler.ico')
root.geometry("750x850")

#listbox
myListbox = Listbox(root, height=40, width=100)
myListbox.pack(pady=15)

#add items from csv file
myList = []

#TODO: get links from csv file on startup
"""
reader = csv.reader(open("links.csv", "r", encoding='utf-8-sig'))
line_count = 0
stop_count = reader.line_num
for row in reader:
    line_count = line_count + 1
    if line_count == 1: #skip the header
        continue
    if line_count > stop_count: #stop at the end
        break
    print(row)
    myList.append(row[6]) #get the link 
"""

for item in myList:
    myListbox.insert(END, item)

def delete():
    myListbox.delete(ANCHOR)

def openLink():
    #TODO: integrate selenium webdriver for opening links
    pass

def popUp():
    top = Toplevel(root)
    top.geometry("500x100")
    top.title("Input")

    # TextBox Creation
    inputtxt = Text(top, height = 4, width = 50)
    inputtxt.pack()

    #inner function for adding link
    def addLink():
        #TODO: add the additional link to the csv file
        #also get the time of the meeting for notifications 
        myListbox.insert(END, inputtxt.get(1.0, "end-1c"))
      
    # Button Creation
    submitButton = Button(top, text = "Submit", command = addLink)
    submitButton.pack()



def scrapeWeb():
    #TODO: integrate web scraping functionality
    pass


openButton = Button(root, text="Open Link", command=openLink)
openButton.pack(pady=5)

delButton = Button(root, text="Delete", command=delete)
delButton.pack(pady=5)

addButton = Button(root, text="Add Link", command=popUp)
addButton.pack(pady=5)

scrapeButton = Button(root, text="Scrape Web", command=scrapeWeb)
scrapeButton.pack(pady=5)

root.mainloop()
