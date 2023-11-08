#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the NYT website to scrape
url = 'https://www.nytimes.com/'

# Send an HTTP request and get the website's content
response = requests.get(url)
html_content = response.text

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the elements containing news article links and their sections
article_elements = soup.find_all('a', {'data-testid': 'article-link'})

# Create lists to store article titles, URLs, and sections
article_titles = []
article_urls = []
article_sections = []

# Iterate through the article elements and extract information
for article in article_elements:
    title = article.get_text()
    link = article['href']
    section = article.find_parent('section').h2.get_text()  # Assuming section information is in an h2 tag

    article_titles.append(title)
    article_urls.append(link)
    article_sections.append(section)

# Limit the number of articles to 100 (or fewer if there are fewer available)
num_articles = min(100, len(article_titles))

# Save the data to a CSV file
with open('nyt_articles.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'URL', 'Section'])

    for i in range(num_articles):
        csv_writer.writerow([article_titles[i], article_urls[i], article_sections[i]])

print(f"{num_articles} articles saved to nyt_articles.csv")


# In[ ]:




