import requests
from bs4 import BeautifulSoup
import csv

url = 'https://g1.globo.com/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all news headlines
    articles = soup.find_all('a', class_='feed-post-link')

    # List to store the data
    news_data = []

    for article in articles:
        title = article.get_text()
        link = article.get('href')  # Use get to avoid KeyError
        if link:
            news_data.append([title, link])

    # Save the data to a CSV file
    with open('Web Scraping - BeautifulSoup and Requests\\g1_news.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])
        writer.writerows(news_data)

    print('Data collected and saved in g1_news.csv')
else:
    print(f'Request error: {response.status_code}')
