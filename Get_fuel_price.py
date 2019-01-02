import requests
import os
import sys
import feedparser
from bs4 import BeautifulSoup
from pprint import pprint
from time import localtime



Fuelinfo_today = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=6'
Fuelinfo_tomorrow = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=6&Day=tomorrow'
FUELTEST = 'file:///Users/leviix/Desktop/Scripts/Python_scripts/Cheap_fuel/Fuelinformation.html'

def menu():
    """A menu for the user to interact with, continous until a correct selection has been made"""
    os.system('clear')
    while True:
        try:
            print('1: Fuelinfo today, 2: Fuelinfo tomorrow, 3: Both today and tomorrow, 4: TEST (localhost), 5: Quit',)
            selector = int(input('Select which data set: ',))

            if selector == 1:
                print('Getting todays fuel prices...')
                selected_data_set = Fuelinfo_today
                return selected_data_set

            elif selector == 2:
                selected_data_set = Fuelinfo_tomorrow
                print('Getting tomorrows fuel prices...')
                return selected_data_set

            elif selector == 3:
                print('Getting both fuel prices...')
                selected_data_set = 'both'
                return selected_data_set

            elif selector == 4:
                print('Getting Test (localhost) fuel prices...')
                selected_data_set = FUELTEST
                return selected_data_set

            elif selector == 5:
                sys.exit(0)
            else:
                print('Input Error: Please select 1 - 5')
        except ValueError:
            print('Value Error: Please select 1 - 5')
            continue


data_to_show = []

def get_data():
    """The main function being called"""
    called_data = menu()
    if called_data == 'both':
        today_data = requests.get(Fuelinfo_today)
        today_parsed = feedparser.parse(today_data.text)
        tomorrow_data = requests.get(Fuelinfo_tomorrow)
        tomorrow_parsed = feedparser.parse(tomorrow_data.text)
        all_parsed = today_parsed.entries + tomorrow_parsed.entries
        return showing(all_parsed)
    elif called_data == FUELTEST:
        print(called_data)
        all_parsed = feedparser.parse(FUELTEST)
        return showing(all_parsed.entries)
    else:
        parse_this = requests.get(called_data)
        all_parsed = feedparser.parse(parse_this.text)
        return showing(all_parsed.entries)


def showing(show_this):
    """Function to append to the list 'data_to_show' given an input of desired fuel day(s)"""
    for entry in show_this:
        data_to_show.append({
            'Store_Name':entry['trading-name'],
            'Price_of_Fuel':entry.price,
            'Location':entry.location,
            'Lat':entry.latitude,
            'Long':entry.longitude,
            'Address':entry.address,
            'Date': entry.date,
            })


get_data()

def sort_Price(data_to_show):
    """sorts any list by the index 'price_of_fuel'"""
    return data_to_show['Price_of_Fuel']


Show_sorted = sorted(data_to_show, key=sort_Price, reverse=True)
pprint(Show_sorted)
print(len(data_to_show))



print('--------------------     ENDED    --------------------')
hour = localtime().tm_hour
minute = localtime().tm_min
second = localtime().tm_sec
print('H:', hour, 'M:', minute, 'S:', second )

# if time <= '2 29':
    # print('Must wait until 2:30pm for tomorrows fuel prices')
# if selected_data_set == 2 ==
