# pip install pytest
import pytest
import csv
import time
from datetime import datetime, date, timedelta
import webbrowser

class TestDateTime:
    def test_0(self):
        # Read from TestFile and pass test if today's weekday is a day that
        # the first appointment would open
        with open("TestFile.csv", "r", encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            line_count = 0
            stop_count = 2
            for row in reader:
                line_count = line_count + 1
                if line_count == 1:
                    continue
                if line_count > stop_count:
                        break
                assert date.today().weekday() == int(row[2])
                
    def test_1(self):
        # If today is Thursday, open Google.com.. else open Bing
        if date.today().weekday() == 3:
            webbrowser.open('https://www.google.com', new=2, autoraise=True)
        else:
            webbrowser.open('https://www.bing.com', new=2, autoraise=True)
            
    def test_2(self):
        # Given a start time, notify 5 minutes prior and auto-open link 1 minute prior.
        str_start_time = input('Enter the time a class starts, in HH:MM format: ')
        dt_start_time = datetime.fromisoformat(date.today().isoformat() + ' ' + str_start_time)
        five_mins_prior = timedelta(hours=0, minutes=5)
        one_min_prior = timedelta(hours=0, minutes=1)
        notification_time = dt_start_time - five_mins_prior
        auto_open_time = dt_start_time - one_min_prior
        curr_time = datetime.now().replace(microsecond=0)
        
        #print('curr_time is', curr_time)
        #print('notification_time is', notification_time)
        #print('auto_open_time is', auto_open_time)
        
        while curr_time < notification_time:
            curr_time = datetime.now().replace(microsecond=0)
            #print('-', curr_time)
            time.sleep(1)
        
        if curr_time >= notification_time:
            #notification.notify(
            #    title = 'Something starts in five minutes!',
            #    message = 'I am so glad this works',
            #    app_icon = None,
            #    timeout = 25
            #)
            print('Notified!')
            
        while curr_time < auto_open_time:
            curr_time = datetime.now().replace(microsecond=0)
            #print('--', curr_time)
            time.sleep(1)
            
        if curr_time >= auto_open_time:
            webbrowser.open('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program', new=2, autoraise=True)
            
