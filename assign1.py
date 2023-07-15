#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2021
Program: assign1.py (replace student_id with your Seneca User name)
Author: Arjun Vadakkekarayil Sojan
The python code in this file (assign1.py) is original work written by
Arjun Vadakkekarayil Sojan. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: July 15th, 2023
'''
import sys
def usage():
    "TODO enter docstring"
    return "Usage: assign1.py <valid date> <number of days>"

def days_in_mon(year):
    "TODO enter docstring"
    # return days
    days_in_mon = {
        1: (31,"January"),
        2: (28,"February"),
        3: (31,"March"),
        4: (30,"April"),
        5: (31,"May"),
        6: (30,"June"),
        7: (31,"July"),
        8: (31,"August"),
        9: (30,"September"),
        10: (31,"October"),
        11: (30,"November"),
        12: (31,"December")
    }

    if leap_year(year):
        days_in_mon[2] = (29,"February")
        return days_in_mon

def valid_date(date):
    "TODO enter docstring"
    # return True or False 
    if len(date)!=10:
        return False
    try:
        day,month,year = map(int,date.split('-'))
    except ValueError:
        return False
    if month not in range(1,13):
        print ("You entered an invalid month. Please enter a valid month between 1 and 12")
        return False
    days_maximum = days_in_mon(year)[month]
    if day not in range(1,days_maximum+1):
        print ("You entered an invalid day. Please enter a valid day for the month")
        return False
    return True

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    # TODO reorganize code, enter code from after() here.
    lyear = year % 4 # TODO: put this into the function leap_year.
    if lyear == 0:
        feb_max = 29 # this is a leap year
        return True
    else:
        feb_max = 28 # this is not a leap year
        

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year
        return False

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year
        return True


def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        tmp_day = day + 1 # next day
        mon_max = days_in_mon(year)
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "TODO enter docstring."
    pass # TODO replace this with code, using your algorithm document.
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        tmp_day = day - 1 # previous day
        mon_max = days_in_mon(year)
        
    if tmp_day < 1:
        prev_mon = True
        if month == 1:
            to_day = mon_max[12]
            to_month = 12
        else:
            to_day = mon_max[month - 1]
            to_month = month - 1
    else:
        prev_mon = False
        to_day = tmp_day
        to_month = month

    if to_month == 12:
        to_month = 12
        if prev_mon:
            year -= 1
    else:
        to_month = tmp_month
    next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
    return next_date

def dbda(start_date, num_days):
    end_date = 0
    # create a loop
    if not valid_date(start_date):
        print("Incorrect date format. Please enter the date in DD-MM-YYYY format")
        return
    # call before() or after() as appropriate
    if num_days>=0:
        next_day = after(start_date)
        print (next_day)
    else:
        prev_day = before(start_date)
        print(prev_day)
    # return end_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    if len(sys.argv) != 3:
        print(usage())
    else:
        start_date = sys.argv[1]
        num_days = int(sys.argv[2])
        dbda(start_date, num_days)
