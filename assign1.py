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

Description: This program accepts a valid date and the number of days as input to calculate the date by adding or subtracting the number from the date. 
If it is positive integer, add the number to the date and if it is a negative integer, reduce the number of days from the inputted date.

Date: July 15th, 2023
'''
import sys
def usage():
    "Returns a string describing the usage of the script."
    return "Usage: assign1.py <valid date> <number of days>"

def days_in_mon(year):
    '''Returns a dictionary object containing the total number of days in each month for the given year.
     Args:
        year (int): The year in "YYYY" format.
    Returns:
        dict: A dictionary object with month numbers (1-12) as keys and the corresponding number of days as values.
    '''
    # return days
    days_in_mon = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if leap_year(year):
        days_in_mon[2] = 29
    return days_in_mon


def valid_date(date):
    '''Checks if the given date is a valid date in "DD-MM-YYYY" format.
    Args:
        date (str): The date string to be validated in "DD-MM-YYYY" format.
    Returns:
        bool: True if the date is valid, False otherwise.'''
    # return True or False 
    
    if len(date)!=10:
       print ("Error: wrong date entered")
       return False
    day,month,year = map(int,date.split('-'))
    if month not in range(1,13):
        print ("Error: wrong month entered")
        return False
    max_days = days_in_mon(year)[month]
    if day not in range(1,max_days):
        print ("Error: wrong day entered")
        return False
    else:
        return True

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    
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

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year).zfill(2)
        return next_date

def before(today):
    '''Returns the date of the previous day in "DD-MM-YYYY" format.
    Args:
        date (str): The date string in "DD-MM-YYYY" format.
    Returns:
        str: The date string representing the previous day in "DD-MM-YYYY" format.'''
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        tmp_day = day - 1 # previous day
        mon_max = days_in_mon(year)
        
    if day > 1:
        previous_month = month
        previous_year = year
    else:
        if month > 1:
            previous_month = month - 1
            previous_year = year
            tmp_day = days_in_mon(previous_year)[previous_month]
        else:
            previous_month = 12
            previous_year = year - 1
            tmp_day = days_in_mon(previous_year)[previous_month]

    next_date = str(tmp_day).zfill(2)+"-"+str(previous_month).zfill(2)+"-"+str(previous_year)
    return next_date

def dbda(start_date, num_days):
    end_date = 0
    # create a loop
    if valid_date(start_date)!=False:
        if num_days>=0:
            end_date = after(start_date)
            for _ in range(num_days-1):
                end_date = after(end_date)
            print (end_date)
        else:
            end_date=before(start_date)
            for _ in range(abs(num_days+1)):
                end_date=before(end_date)
            print (end_date)


    '''while valid_date(start_date)!=False:
    # call before() or after() as appropriate
        if num_days>=0:
            for _ in range(num_days-1):
                end_date = after(end_date)
                print (end_date)
        else:
            for _ in range(abs(num_days+1)):
                end_date=before(end_date)
                print (end_date)
    # return end_date'''

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(usage())
    else:
        start_date = sys.argv[1]
        num_days = int(sys.argv[2])
        end_date = dbda(start_date, num_days)
        #print (end_date)
