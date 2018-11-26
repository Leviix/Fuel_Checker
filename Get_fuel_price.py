import requests
import os
import time
import feedparser
from bs4 import BeautifulSoup
from pprint import pprint
# os.system('clear')

Fuelinfo_today = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2'
Fuelinfo_tomorrow = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Day=tomorrow'
FUELTEST = 'file:///Users/leviix/Desktop/Scripts/Python_scripts/Cheap_fuel/Fuelinformation.html' #open('Fuelinformation.html','r+')

### selector/menu
def menu():
    """A menu for the user to interact with, continous until a correct selection has been made"""
    # Fuelinfo_today = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2'
    # Fuelinfo_tomorrow = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Day=tomorrow'
    # FUELTEST = open('/Users/leviix/Desktop/Scripts/Python_scripts/Cheap_fuel/Fuelinformation.html', mode='w')

    os.system('clear')
    while True:
        try:
            print('1: Fuelinfo today, 2: Fuelinfo tomorrow, 3: Both today and tomorrow, 4: TEST (localhost), 5: Quit',)
            selector = int(input('Select which data set: ',))

            if selector == 1:
                print('Getting todays fuel prices...')
                selected_data_set = Fuelinfo_today
                return selected_data_set
                break

            elif selector == 2:
                selected_data_set = Fuelinfo_tomorrow
                print('Getting tomorrows fuel prices...')
                return selected_data_set
                break

            elif selector == 3:
                print('Getting both fuel prices...')
                selected_data_set = [Fuelinfo_today, Fuelinfo_tomorrow]
                return selected_data_set
                break

            elif selector == 4:
                print('Getting Test (localhost) fuel prices...')
                selected_data_set = FUELTEST
                return selected_data_set
                break

            elif selector == 5:
                # except InvalidURL
                noreturn = ('http:///None?')
                return noreturn
                break
            else:
                print('Input Error: Please select 1 - 5')
        except ValueError:
            print('Value Error: Please select 1 - 5')
            continue

# menu()
###
# print('THIS IS THE PRINT STATEMENT', menu(), "second time maybe #so confused",)

def get_data():
    selected_data_set = menu()
    if selected_data_set == FUELTEST:
        print(selected_data_set)
        parsed_info = feedparser.parse(FUELTEST)
        # return parsed_info
    else:
        grabbed_data = requests.get(selected_data_set)
        parsed_info = feedparser.parse(grabbed_data.text)
        # return parsed_info

    for entries in parsed_info.entries:
        print(entries.title, entries.address)
        both_data_sets.append(entries.title)

### change atibute to selected_data_set when menu is working
# grabbed_data = requests.get(selected_data_set)


### Put any grabbed data through a parser to read and manipulate it better
# parsed_info = feedparser.parse(grabbed_data.text)


###
# Sting manipulation
both_data_sets = []

get_data()


# for entries in fuel_Formatted(grabbed_data).entries:

print('--------------------ENDED HERE--------------------')

# print(both_data_sets)



#
# for title in fuel_e.find_all('title'):
#     values = []
#     data.append(values)
# #
# def fuel_Brands(website):
#     brandselect = input('Please select a brand: ',)
#     brands = requests.get(website + '?Brand=' + str(brandselect))
#     return feedparser.parse(brands.content)
#
# def fuel_Type(website):
#     fueltype = input('Please select a type of fuel: ',)
#     brands = requests.get(website + '?Product=' + str(fueltype))
#     return feedparser.parse(brands.content)
#
# def fuel_Address(website):
#     brands = requests.get(website + '?Brand=')
#     return feedparser.parse(brands.content)
#
# def get_fuel_price(website):
#     brandselect = input('Please select a brand')
#     brands = requests.get(website + '?Brand=' + brandselect)
#     return feedparser.parse(brands.content)
# ##
