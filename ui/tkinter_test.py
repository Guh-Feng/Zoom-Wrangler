from tkinter import *
from ZoomConnect import open_meeting
import csv

root = Tk()
root.title('Zoom Wrangler')
#root.iconbitmap('wrangler.ico')
root.geometry("750x850")




#listboxes
myListbox = Listbox(root, height=40, width=100)
myListbox.pack(pady=15)

#add items from csv file
myList = []

'''
reader = csv.reader(open("links.csv", "r", encoding='utf-8-sig'))
print("opened")
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
'''

#write info from CSV into list
with open('links.csv', 'r') as read_obj:
    reader = csv.reader(read_obj)
    myList = list(reader)

#write data from list into UI
#header
fhead = myList[0][0]
myListbox.insert(END, f"{fhead[3:]:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}" )
#myListbox.insert(END, f"{hellomn:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}" )
#print(f"{fhead[3:]:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}")
#rest of items

#known issue, whitespace is not the same length as characters, makes weird issues with formatting
for x in range(1,len(myList)):
    myListbox.insert(END, f"{myList[x][0]:<20} {myList[x][1]:<45} {myList[x][5]:<15} {myList[x][6]}")



#TODO: schedule notifcations in list



def delete():
    myListbox.delete(ANCHOR)

def openLink():
    #TODO: integrate selenium webdriver for opening links
    #TODO: verificiation that input from listbox is only a zoom link, or pass in only a zoom link
    open_meeting(myListbox.get(myListbox.curselection()))

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
        top.destroy()

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
