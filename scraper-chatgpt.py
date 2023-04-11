import requests
import csv
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.imdb.com/?ref_=nv_home"
response = requests.get(url)
html = response.text

# Parse the HTML code
soup = BeautifulSoup(html, 'html.parser')

# Extract the desired data
titles = soup.find_all('h3', {'class': 'lister-item-header'})

# Open a CSV file for writing
with open('movie_titles.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the movie titles to the CSV file
    for title in titles:
        movie_title = title.find('a').text
        writer.writerow([movie_title])
