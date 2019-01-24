import requests
import os
import sys
import feedparser
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

def showing(show_this, colour = 0):
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
    if result_pM == 8:
        test_parsed = feedparser.parse(FUELTEST)
        return showing(test_parsed)
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
    # table_Creation(all_parsed)
    return all_parsed

if __name__ == __name__:
    get_data()

Show_sorted = sorted(data_to_show, key=sort_Price, reverse=True)
# pprint(Show_sorted)


pprint(Show_sorted)
print(len(data_to_show))
def table_Creation(data):


    f = open('table.html', 'w')
    table_stuff = '''
    <table>
        <thead>
            <tr>
                <th colspan = '5'> Fuel Scrapped</th>
            </tr>
            <tr>
                <td> Store Name </td>
                <td> Price </td>
                <td> Address </td>
                <td> Location </td>
                <td> Date </td>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>{sn}</td>
                <td>{p}</td>
                <td>{a}</td>
                <td>{l}</td>
                <td>{d}</td>
            </tr>
        </tbody>
    </table>
    '''

    for entry in data:
        table_stuff.format(sn=entry['Address'],
                        p=entry['Price_of_Fuel'],
                        a=entry['Address'],
                        l=entry['Address'],
                        d=entry['Date'])
    # for entry in data:
    #     P =+ entry['Price_of_Fuel']
    # for entry in data:
    #     A =+ entry['Address']
    # for entry in data:
    #     L = entry['Location']
    # for entry in data:
    #     D = entry['Date']




    title = '''
        <head>
            <title>
                Fuel Scrapper
            </title>
        </head>
        '''

    body = '''
        <h1>Fuel Scrapepd.</h1>
        <p>Paragraph {}.</p>
    '''.format(data)

    f.write(title + table_stuff + body)
    f.close()


table_Creation(data_to_show)



print(':-----------:-----------: ENDED HERE :-----------:-----------:')
H = localtime().tm_hour
M = localtime().tm_min
S = localtime().tm_sec
print('Time: {}:{}:{}'.format(H, M, S))
