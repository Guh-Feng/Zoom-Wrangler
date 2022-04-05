# pip install pytest
import pytest
import csv

class TestCSV:
    def test_0(self):
        # open and read the first line (header)
        with open("TestFile.csv", "r", encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            line_count = 0
            stop_count = 1
            for row in reader:
                line_count = line_count + 1
                if line_count > stop_count:
                        break
                assert row == ['Class Code', 'Class Name', 'Day of week (0 = Monday, 1 = Tuesday..)',
                               'Notification Time', 'Auto-Open Time', 'Start Time', 'Link']

                
    def test_1(self):
        # open and read the second line
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
                assert row == ['CEN3031', 'Software Engineering, Intro to', '2', '14:55', '14:59', 
                               '15:00', 'https://ufl.zoom.us/j/99700198187']

    def test_2(self):
        # write and append into the CSV file
        with open("TestFile.csv", "a", encoding='utf-8-sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            zoom_object = ['CIS4930', 'Special Topics', '16:00', '16:04', '16:05', 'https://ufl.zoom.us/j/92738786613?pwd=VXZlUnduUGFMVzZhV2hLVmtMN1ptQT09']
            writer.writerow(zoom_object)
        with open("TestFile.csv", "r", encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            line_count = 0
            stop_count = reader.line_num
            for row in reader:
                line_count = line_count + 1
                if line_count == 1:
                    continue
                if line_count > stop_count:
                    break
                assert row == ['CIS4930', 'Special Topics', '16:00', '16:04', '16:05', 
                               'https://ufl.zoom.us/j/92738786613?pwd=VXZlUnduUGFMVzZhV2hLVmtMN1ptQT09']
