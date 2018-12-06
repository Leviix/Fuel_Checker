import requests
import os
import sys
import feedparser
from bs4 import BeautifulSoup
from pprint import pprint
from time import localtime

Fuelinfo_today = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2'
Fuelinfo_tomorrow = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Day=tomorrow'
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
                selected_data_set = [Fuelinfo_today, Fuelinfo_tomorrow]
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
        # except ConnectionError:
            # print('Not connected to the internet, check connection and try again')
# menu()
###

combined_sets = []
def get_data():
    selected_data_set = menu()
    if selected_data_set == FUELTEST:
        print(selected_data_set)
        parsed_info = feedparser.parse(FUELTEST)

    elif selected_data_set == []:
        pass


    else:
        grabbed_data = requests.get(selected_data_set)
        parsed_info = feedparser.parse(grabbed_data.text)

    for entries in reversed(parsed_info.entries):
        print(entries.title, entries.address)
        combined_sets.append(entries.title)

get_data()


# for entries in fuel_Formatted(grabbed_data).entries:

print('--------------------     ENDED    --------------------')
# print(localtime().tm_hour)
# print(localtime().tm_min)
hour = localtime().tm_hour
minute = localtime().tm_min
print('H',hour,': M', minute)

# if time <= '2 29':
    # print('Must wait until 2:30pm for tomorrows fuel prices')
# if selected_data_set == 2 ==

# print(both_data_sets)
