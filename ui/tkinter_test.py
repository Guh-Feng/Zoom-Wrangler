from tkinter import *
from ZoomConnect import open_meeting
import csv

root = Tk()
root.title('Zoom Wrangler')
#root.iconbitmap('wrangler.ico')
root.geometry("750x850")


# function to overwrite the CSV from the current myList - actual tracking of each row
def writeList():
    f = open('links.csv', "w+")
    f.close()
    file = open('links.csv', 'a+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(myList)


# listboxes created from CSV here
myList = []
myListbox = Listbox(root, height=35, width=100)
myListbox.pack(pady=15)

    #write info from CSV into myList
with open('links.csv', 'r') as read_obj:
    reader = csv.reader(read_obj)
    myList = list(reader)

    #write data from list into UI

    # header on myListBox
fhead = myList[0][0]
#fhead[3:] if error on head
myListbox.insert(END, f"{fhead:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}" )
    #myListbox.insert(END, f"{hellomn:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}" )
    #print(f"{fhead[3:]:<20} {myList[0][1]:<45} {myList[0][5]:<15} {myList[0][6]}")


    # every row printed into myListBox
    # known issue, whitespace is not the same length as characters, makes weird issues with formatting
for x in range(1,len(myList)):
    myListbox.insert(END, f"{myList[x][0]:<20} {myList[x][1]:<45} {myList[x][5]:<15} {myList[x][6]}")

#TODO:  schedule notifcations in list

# delete button functionality
def delete():
    selection = myListbox.curselection()[0]
    if selection == 0:
        return
    del myList[selection]
    myListbox.delete(ANCHOR)
    writeList()


# Opens link from myList on selected row
def openLink():
    #TODO: verificiation that input from listbox is only a zoom link, or pass in only a zoom link (is this needed?)
    selection = myListbox.curselection()[0]
    if selection == 0:
        return
    #print(myList[selection][6])
    open_meeting((myList[selection][6]))
    pass

<<<<<<< Updated upstream
=======
def popUp():
<<<<<<< Updated upstream
    top = Toplevel(root)
    top.geometry("500x100")
    top.title("Input")
>>>>>>> Stashed changes

def popUp():
    # Create new window
    topp = Toplevel(root)
    topp.geometry("800x300")
    topp.title("Input")

    # TextBox creation for inputs
    inpt0 = Text(topp, height = 1, width = 50)
    inpt0.insert(INSERT, "<Class Code>")
    inpt0.pack()
    inpt1 = Text(topp, height = 1, width = 50)
    inpt1.insert(INSERT, "<Class Name>")
    inpt1.pack()
    inpt2 = Text(topp, height = 1, width = 50)
    inpt2.insert(INSERT, "<Meeting Day>")
    inpt2.pack()
    inpt3 = Text(topp, height = 1, width = 50)
    inpt3.insert(INSERT, "<Meeting Time>")
    inpt3.pack()
    inpt4 = Text(topp, height = 1, width = 50)
    inpt4.insert(INSERT, "<Meeting Link>")
    inpt4.pack()

    #inner function for adding link
    def addLink():
<<<<<<< Updated upstream
=======
        #TODO: add the additional link to the csv file
        #also get the time of the meeting for notifications
        myListbox.insert(END, inputtxt.get(1.0, "end-1c"))
        top.destroy()
=======
    # Create new window
    topp = Toplevel(root)
    topp.geometry("800x300")
    topp.title("Input")

    # TextBox creation for inputs
    inpt0 = Text(topp, height = 1, width = 50)
    inpt0.insert(INSERT, "<Class Code>")
    inpt0.pack()
    inpt1 = Text(topp, height = 1, width = 50)
    inpt1.insert(INSERT, "<Class Name>")
    inpt1.pack()
    inpt2 = Text(topp, height = 1, width = 50)
    inpt2.insert(INSERT, "<Meeting Day (0 = Monday, 1 = Tuesday..)>")
    inpt2.pack()
    inpt3 = Text(topp, height = 1, width = 50)
    inpt3.insert(INSERT, "<Meeting Time>")
    inpt3.pack()
    inpt4 = Text(topp, height = 1, width = 50)
    inpt4.insert(INSERT, "<Meeting Link>")
    inpt4.pack()

    #inner function for adding link
    def addLink():
>>>>>>> Stashed changes

        #TODO: also get the time of the meeting for notifications, maybe schedule here?

        # Small error check to see if inputs were missed
<<<<<<< Updated upstream
        if inpt0.get(1.0, "end-1c") == "<Class Code>" or inpt1.get(1.0, "end-1c") == "<Class Name>" or inpt2.get(1.0, "end-1c") == "<Meeting Day>" or inpt3.get(1.0, "end-1c") == "<Meeting Time>" or inpt4.get(1.0, "end-1c") == "<Meeting Link>":
=======
        if inpt0.get(1.0, "end-1c") == "<Class Code>" or inpt1.get(1.0, "end-1c") == "<Class Name>" or inpt2.get(1.0, "end-1c") == "<Meeting Day (0 = Monday, 1 = Tuesday..)>" or inpt3.get(1.0, "end-1c") == "<Meeting Time>" or inpt4.get(1.0, "end-1c") == "<Meeting Link>":
>>>>>>> Stashed changes
            top = Toplevel(root)
            top.geometry("300x100")
            top.title("Error!")
            errtxt = Text(top, height = 1, width = 30)
            errtxt.insert(INSERT, "Error! Check your inputs")
            errtxt.pack()
            return

        # Append to myList and myListBox
        myList.append([inpt0.get(1.0, "end-1c"),inpt1.get(1.0, "end-1c"),inpt2.get(1.0, "end-1c"),inpt3.get(1.0, "end-1c"),inpt3.get(1.0, "end-1c"),inpt3.get(1.0, "end-1c"),inpt4.get(1.0, "end-1c")])

        mlSize = len(myList) - 1
        myListbox.insert(END, f"{myList[mlSize][0]:<20} {myList[mlSize][1]:<45} {myList[mlSize][5]:<15} {myList[mlSize][6]}")
        writeList()
        topp.destroy()

<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
>>>>>>> Stashed changes

    # Button Creation
    submitButton = Button(topp, text = "Submit", command = addLink)
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
