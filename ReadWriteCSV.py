import csv
import webbrowser
from datetime import datetime, date, timedelta
from tkinter import *

class Database:
    def __init__(self, passed_links, file_name, is_new = True, ):
        self.file_name = file_name
        """
        if is_new:
            self.file_name = input('Please input name of the new database file: ')
        else:
            self.file_name = input('Please input name of the database file: ')
        """
        if self.file_name[-4:] != '.csv':
            self.file_name = self.file_name + '.csv'
        with open(self.file_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if is_new:
                writer.writerow(['Class Code', 'Class Name', 'Day of week (0 = Monday, 1 = Tuesday..)',
                                'Notification Time', 'Auto-Open Time', 'Start Time', 'Link'])
            #print('Found', len(passed_links), 'link(s)!')
            for links in passed_links:
                #print('\nFound Zoom link:', link)
                #global looping
                #looping = True
                #while looping:
                def yes():
                    top.destroy()
                    def submit():
                        # Get user input about this appointment
                        row = []
                        row.append(code.get(1.0, "end-1c"))
                        row.append(name.get(1.0, "end-1c"))
                        row.append(day.get(1.0, "end-1c"))
                        start_time = time.get(1.0, "end-1c")
                        mins_before_notif = notif.get(1.0, "end-1c")
                        mins_before_auto_open = op.get(1.0, "end-1c")
                        
                        # Create datetime objects, can easily maniupulate using timedelta
                        dt_start_time = datetime.fromisoformat(date.today().isoformat() + ' ' + start_time)
                        dt_notif_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_notif))
                        dt_auto_open_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_auto_open))
                        
                        # Strings to put into database for storage
                        db_start_time = dt_start_time.isoformat(timespec = 'minutes').replace(date.today().isoformat(), '')
                        db_notif_time = dt_notif_time.isoformat(timespec = 'minutes').replace(date.today().isoformat(), '')
                        db_auto_open_time = dt_auto_open_time.isoformat(timespec='minutes').replace(date.today().isoformat(), '')
                        
                        row.append(db_notif_time)
                        row.append(db_auto_open_time)
                        row.append(db_start_time)
                        row.append(links)
                        writer.writerow(row)

                        top2.destroy()

                    top2 = Tk()
                    top2.geometry("350x250")
                    top2.title("Information")

                    code = Text(top2, height=1, width = 35)
                    code.insert(INSERT, "<class code>")
                    code.pack()

                    name = Text(top2, height=1, width = 35)
                    name.insert(INSERT, "<class name>")
                    name.pack()

                    day = Text(top2, height=1, width = 35)
                    day.insert(INSERT, "<day of week> [0=Mon, 1=Tues,...]")
                    day.pack()

                    time = Text(top2, height=1, width = 35)
                    time.insert(INSERT, "<start time (HH:MM)>")
                    time.pack()

                    notif = Text(top2, height=1, width = 35)
                    notif.insert(INSERT, "<mins before notification>")
                    notif.pack()

                    op = Text(top2, height=1, width = 35)
                    op.insert(INSERT, "<mins before opening>")
                    op.pack()

                    subButton = Button(top2, text = "Submit", command = submit)
                    subButton.pack()


                def no():
                    top.destroy()
                    

                top = Tk()
                top.geometry("500x200")
                top.title("Add link")
                
                txt = Text(top, height = 2, width = 28)
                txt.insert(INSERT, "Continue adding this link?")
                txt.pack()

                link = Label(top, text=str(links))
                #link = Text(top, height = 1, width = 200)
                #link.insert(INSERT, str(link))
                link.pack()

                yesButton = Button(top, text = "Yes", command = yes)
                yesButton.pack()

                noButton = Button(top, text = "No", command = no)
                noButton.pack()

                top.mainloop()


                """
                    
                    #choice = input("\nContinue adding this link to database? (Y/N) ")
                    
                    if choice.capitalize() == 'N':
                        looping = False
                        break
                    elif choice.capitalize() == 'Y':
                        # Get user input about this appointment
                        row = []
                        row.append(input("Class Code: "))
                        row.append(input("Class Name: "))
                        row.append(input("Day of week (0 = Monday, 1 = Tuesday..): "))
                        start_time = input("Start Time (HH:MM): ")
                        mins_before_notif = input("How many minutes before the start time should we send a notification? ")
                        mins_before_auto_open = input("How many minutes before the start time should we auto-open the link? ")
                        
                        # Create datetime objects, can easily maniupulate using timedelta
                        dt_start_time = datetime.fromisoformat(date.today().isoformat() + ' ' + start_time)
                        dt_notif_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_notif))
                        dt_auto_open_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_auto_open))
                        
                        # Strings to put into database for storage
                        db_start_time = dt_start_time.isoformat(timespec = 'minutes').replace(date.today().isoformat(), '')
                        db_notif_time = dt_notif_time.isoformat(timespec = 'minutes').replace(date.today().isoformat(), '')
                        db_auto_open_time = dt_auto_open_time.isoformat(timespec='minutes').replace(date.today().isoformat(), '')
                        
                        row.append(db_notif_time)
                        row.append(db_auto_open_time)
                        row.append(db_start_time)
                        row.append(link)
                        writer.writerow(row)
                        break
                    else:
                        print('Invalid input!')
                        continue
            """
                
    def fetch(self, row_count):
        with open(self.file_name, "r", encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            line_count = 0
            stop_count = row_count
            for row in reader:
                line_count = line_count + 1
                if line_count == 1:
                    continue
                if line_count > stop_count:
                    break
            return row
