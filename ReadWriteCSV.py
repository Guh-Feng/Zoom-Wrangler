import csv
import webbrowser
from datetime import datetime, timedelta

class Database:
    def __init__(self, passed_links, is_new = True):
        file_name = ''
        if is_new:
            file_name = input('Please input name of the new database file: ')
        else:
            file_name = input('Please input name of the database file: ')
        file_name = file_name + '.csv'
        with open(file_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if is_new:
                writer.writerow(['Class Code', 'Class Name', 'Day of week (0 = Monday, 1 = Tuesday..)',
                                'Notification Time', 'Auto-Open Time', 'Start Time', 'Link'])
            for link in passed_links:
                print('Found Zoom link: ', link)
                while True:
                    choice = input("Continue adding this link to database? (Y/N) ")
                    if choice.capitalize() == 'N':
                        break
                    elif choice.capitalize() == 'Y':
                        row = []
                        row.append(input("Class Code: "))
                        row.append(input("Class Name: "))
                        row.append(input("Day of week (0 = Monday, 1 = Tuesday..): "))
                        start_time = input("Start Time (HH:MM): ")
                        mins_before_notif = input("How many minutes before the start time should we send a notification? ")
                        mins_before_auto_open = input("How many minutes before the start time should we auto-open the link? ")
                        dt_start_time = datetime.fromisoformat(start_time)
                        dt_notif_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_notif))
                        dt_auto_open_time = dt_start_time - timedelta(hours = 0, minutes = int(mins_before_auto_open))
                        row.append(dt_notif_time.isoformat(timespec = 'minutes'))
                        row.append(dt_auto_open_time.isoformat(timespec = 'minutes'))
                        row.append(dt_start_time.isoformat(timespec = 'minutes'))
                        row.append(link)
                        writer.writerow(row)
                        break
                    else:
                        print('Invalid input!')
                        continue