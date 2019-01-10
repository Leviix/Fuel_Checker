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
    """meant to create and the required urls for both today and tomororw and return it"""

    url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={prod}&Day={day}'



    modded_url = url.format(prod= , day)

    return modded_url



















data_to_show = []


def get_data():
    """The main function being called.......aka Main"""

    moded_Url(prod=prod_Men(), )

    if  x == 'both':
        today_data = requests.get(URl)
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


def sort_Price(data_to_show):
    """sorts any list by the key 'price_of_fuel', meant to work in tangent with sort_Price() function"""
    return data_to_show['Price_of_Fuel']


Show_sorted = sorted(data_to_show, key=sort_Price, reverse=True)
pprint(Show_sorted)
print(len(data_to_show))


get_data()


print('--------------------     ENDED    --------------------')
H = localtime().tm_hour
M = localtime().tm_min
S = localtime().tm_sec
print('H:{}, S:{}, M:{}'.format(H, M, S))

# if time <= '2 30':
    # print('Must wait until 2:30pm for tomorrows fuel prices')
# if selected_data_set == 2 ==
