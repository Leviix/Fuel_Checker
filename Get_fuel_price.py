import requests
import os
import sys
import feedparser
from bs4 import BeautifulSoup
from pprint import pprint
from time import localtime
from Product_Menu import product_Menu as prod_Men



FUELTEST = 'file:///Users/leviix/Desktop/Scripts/Python_scripts/Cheap_fuel/Fuelinformation.html'

def moded_Url(prod, day):
    """meant to create the required urls for both today and tomororw and return it"""

    url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={product}&Day={days}'
    modded_url = url.format(product=prod , days=day)
    return modded_url

data_to_show = []
def showing(show_this, colour):
    """Function to append to the list 'data_to_show' given an input of desired fuel day(s)"""
    if colour == 'Tomorrow':
        pass

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

def sort_Price(data_to_show):
    """sorts any list by the key 'price_of_fuel', meant to work in tangent with sort_Price() function"""
    return data_to_show['Price_of_Fuel']

def get_data():
    """The main function being called.......aka Main."""

    result_pM = prod_Men()
    day_Z = ['Today', 'Tomorrow']
    today_url = moded_Url(result_pM, day_Z[0])
    tomorrow_url = moded_Url(result_pM, day_Z[1])

    try:
        today_data = requests.get(today_url)
        tomorrow_data = requests.get(tomorrow_url)
    except requests.exceptions.ConnectionError:
        print('\n:----:----: Unabel to connect to the internt :----:----:\
            \nPlease check your internet connection and try again.\n\n')
        sys.exit(0)
    today_parsed = feedparser.parse(today_data.text)
    tomorrow_parsed = feedparser.parse(tomorrow_data.text)
    colour_this = tomorrow_url[-8:]
    all_parsed = today_parsed.entries + tomorrow_parsed.entries
    showing(all_parsed, colour_this)

get_data()


Show_sorted = sorted(data_to_show, key=sort_Price, reverse=True)
pprint(Show_sorted)
print(len(data_to_show))



print(':-----------:-----------: ENDED HERE :-----------:-----------:')
H = localtime().tm_hour
M = localtime().tm_min
S = localtime().tm_sec
print('H:{}, S:{}, M:{}'.format(H, M, S))

# if time <= '2 30':
    # print('Must wait until 2:30pm for tomorrows fuel prices')
# if selected_data_set == 2 ==
