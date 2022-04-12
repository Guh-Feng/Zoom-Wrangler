"""
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
"""



"""
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Add Link", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Open Meeting", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

"""



#textbox for input
"""
import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
"""



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

with open("links.csv", "r", encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
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
