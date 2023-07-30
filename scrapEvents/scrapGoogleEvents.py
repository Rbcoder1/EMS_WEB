import json
import requests
from bs4 import BeautifulSoup


allevent = []
# Set the URL of the events page


def GenerateGoogleEvent():
    print("Proccess of Generating Google Events Take Some Time......")
    url = 'https://cloud.google.com/events'

    # Send a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    print("Fetting Data From Google ......")
    # print(html_content)
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all event cards on the page
    event_cards = soup.find_all(
        'li', {'class': 'Qwf2Db-kR0ZEf-OWXEXe-GV1x9e-II5mzb Qwf2Db-kR0ZEf-OWXEXe-GV1x9e-qWD73c-V2iZpe Qwf2Db-kR0ZEf-OWXEXe-GV1x9e-II5mzb-UFsB2c'})

    print("Fetch Events From Google ........")
    # print(event_cards)
    # Loop through the event cards and print the title, date, and location of each event
    for card in event_cards:

        link = card.find('a', {'class': 'Qwf2Db-WsjYwc JadhYc'})
        event = {
            "title": card.find('p', {'class': 'Qwf2Db-MnozTc Qwf2Db-MnozTc-OWXEXe-MnozTc-wNfPc'}).text.strip().replace("\u2009\u2013\u2009", ""),
            "desc": card.find('div', {'class': 'Qwf2Db-qJTHM'}).text.strip().replace("\u2009\u2013\u2009", "").replace("\u2019\u00e9", ""),
            "img": 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjzC2JyZDZ_RaWf0qp11K0lcvB6b6kYNMoqtZAQ9hiPZ4cTIOB',
            "organizer":  ['google'],
            "start_date": card.find('div', {'class': 'Qwf2Db-DbgRPb-ibL1re-OWXEXe-ma6Yeb Qwf2Db-DbgRPb-ibL1re-OWXEXe-cGMI2b'}).text.replace("\u2009\u2013\u2009", "-"),
            "duration": card.find('div', {'class': 'quZrde'}).text.strip(),
            "link":  link.get('href')
        }

        allevent.append(event)

    EventObj = {
        "allEvents" : allevent
    }
    
    print("Google Event Generated Successfully .")
    print("Storing in Json File ......")

    with open("./Events/Google.json", "w") as file:
        json.dump(EventObj, file)

    print("Done")