import csv
import webbrowser
from datetime import datetime, date, timedelta

class Database:
    def __init__(self, passed_links, is_new = True, print = False):
        self.file_name = ''
        self.entry_count = 0
        self.prev_count = 0
        if is_new:
            file_name = input('Please input name of the new database file: ')
        else:
            self.file_name = input('Please input name of the database file: ')
            self.prev_count = self.entry_count
        self.file_name = self.file_name + '.csv'
        if passed_links:
            with open(self.file_name, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if is_new:
                    writer.writerow(['Class Code', 'Class Name', 'Day of week (0 = Monday, 1 = Tuesday..)',
                                    'Notification Time', 'Auto-Open Time', 'Start Time', 'Link'])
                print('Found', len(passed_links), 'link(s)!')
                for link in passed_links:
                    print('\nFound Zoom link:', link)
                    looping = True
                    while looping:
                        choice = input("\nContinue adding this link to database? (Y/N) ")
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
                            self.entry_count = self.entry_count + 1
                            break
                        else:
                            print('Invalid input!')
                            continue
        elif not print:
            with open(self.file_name, "r", encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile)
                line_count = 0
                stop_count = self.num_entries
                for row in reader:
                    line_count = line_count + 1
                    if line_count == 1:
                        continue
                    if line_count > stop_count:
                        break
                    print(row)
        else:
            with open(self.file_name, "r", encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile)
                self.num_entries = reader.line_num - 1
    
    def fetch_row(self, row_count):
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
    
    def num_entries(self):
        return self.entry_count

    def diff_entries(self):
        return self.entry_count - self.prev_count