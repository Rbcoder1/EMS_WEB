import json
import requests
from bs4 import BeautifulSoup


allevent = []
# Set the URL of the events page


def GenerateH2SEvents():
    print("Proccess of Generating Hack2Skill Events Take Some Time......")

    url = 'https://hack2skill.com'

    allevent = []
    # Send a request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    print("Fetting Data From H2S ......")

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all event cards on the page
    event_cards = soup.find_all(
        'div', {'class': 'swiper-slide newCard'})

    print("Fetch Events From H2S ........")

    for card in event_cards:
        link = card.find('a', {'class': 'text-link'})
        img = card.find('img', {'class': 'card-img-top border-bottom'})
        event = {
            "title": card.find('h6').text.strip(),
            "desc": card.find('p', {'class': 'hack-description'}).text.strip(),
            "img": img.get('src'),
            "organizer":  ['Hack2Skill'],
            "submmision_date": card.find('p', {'class': 'last-date'}).text.strip(),
            "Mode": card.find('div', {'class': 'float-right'}).text.strip(),
            "link":  link.get('href')
        }
        allevent.append(event)

        EventObj = {
            "allEvents": allevent
        }

    print("Hack2Skill Event Generated Successfully .")
    print("Storing in Json File ......")

    with open("./Events/H2S.json", "w") as file:
        json.dump(EventObj, file)

    print("done")
