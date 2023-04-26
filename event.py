# # import requests
# # from bs4 import BeautifulSoup
# # import json

# # # URL to scrape
# # url = 'https://aws.amazon.com/training/events/?nc2=h_ql_ev_lf&get-certified-vilt-courses-cards.sort-by=item.additionalFields.startDateSort&get-certified-vilt-courses-cards.sort-order=asc&awsf.get-certified-vilt-courses-type=*all&awsf.get-certified-vilt-courses-series=*all&awsf.get-certified-vilt-audience=*all&awsf.get-certified-vilt-locations=*all&awsf.get-certified-vilt-countries=*all&awsf.get-certified-vilt-languages=*all&awsf.get-certified-vilt-courses-level=*all&awsf.get-certified-vilt-courses-tech-category=*all'

# # # Send GET request to the URL
# # response = requests.get(url)

# # # Parse the HTML content
# # soup = BeautifulSoup(response.content, 'html.parser')

# # # Find all event containers
# # event_containers = soup.find("ul", class_="aws-directories-container lb-xb-grid lb-row-max-large lb-snap lb-tiny-xb-1 lb-small-xb-2 lb-large-xb-3 lb-xb-equal-height lb-vgutter-collapse")

# # print(event_containers)


# # # List to store event data
# # events = []

# # # Loop through each event container
# # for event_container in event_containers:
# #     event = {}
# #     event["title"] = event_container.find("h2").text.strip()
# #     event["location"] = event_container.find("p", class_="aws-text-nowrap").text.strip()
# #     event["date"] = event_container.find("span", class_="aws-text-color-grey").text.strip()
# #     event["image_url"] = event_container.find("img")["src"]
# #     events.append(event)

# # # Store events data in a JSON file
# # with open('events.json', 'w') as json_file:
# #     json.dump(events, json_file, indent=4)

# # print("Events data has been scraped and stored in events.json file.")



# import requests
# from bs4 import BeautifulSoup

# # URL to scrape
# url = 'https://aws.amazon.com/government-education/events/'

# # Send a GET request to the URL and get the response
# response = requests.get(url)
# t=response.text
# with open("./event.html", "w",encoding='utf-8') as h:
#     h.write(t)


# # Parse the HTML content using 'html5lib' parser
# soup = BeautifulSoup(response.content, 'html5lib')

# # Find the container element that holds the event information
# event_container = soup.find('ul', {'role': 'tablist'})



# print(event_container)
# # Initialize an empty list to store the events
# events_list = []

# # Loop through each event element within the container
# for event_element in event_container.find_all('div', {'class': 'lb-col lb-col-md-6 lb-col-lg-4 training-upcomingEvents-item'}):
#     # Extract the relevant information from the event element
#     event_title = event_element.find('div', {'class': 'training-upcomingEvents-title'}).text.strip()
#     event_location = event_element.find('div', {'class': 'training-upcomingEvents-location'}).text.strip()
#     event_date = event_element.find('div', {'class': 'training-upcomingEvents-date'}).text.strip()

#     # Create a dictionary to store the event information
#     event = {
#         'title': event_title,
#         'location': event_location,
#         'date': event_date
#     }

#     # Append the event dictionary to the events list
#     events_list.append(event)

# # Print the list of events
# print(events_list)



from selenium import webdriver
from bs4 import BeautifulSoup

# Create a new instance of the Firefox driver (you can use other drivers as well)
driver = webdriver.Firefox()

# Navigate to the URL
url = 'https://aws.amazon.com/government-education/events/'
driver.get(url)

# Get the page source after JavaScript rendering
page_source = driver.page_source

print(page_source)

# Parse the HTML content of the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the container element that holds the event information
event_container = soup.find('div', {'class': 'lb-row training-upcomingEvents-list'})

# Extract event information from the event container
# (replace this with your actual code for extracting the desired data)
events = []
for event_elem in event_container.find_all('div', {'class': 'training-upcomingEvents-item'}):
    event = {}
    event['title'] = event_elem.find('div', {'class': 'training-upcomingEvents-item-title'}).text.strip()
    event['date'] = event_elem.find('div', {'class': 'training-upcomingEvents-item-date'}).text.strip()
    event['location'] = event_elem.find('div', {'class': 'training-upcomingEvents-item-location'}).text.strip()
    events.append(event)

# Close the driver
driver.quit()

# Print the scraped event data
for event in events:
    print('Title:', event['title'])
    print('Date:', event['date'])
    print('Location:', event['location'])
    print()
