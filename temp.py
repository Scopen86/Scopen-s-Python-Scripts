import requests
from bs4 import BeautifulSoup

# URL of the main page containing the keyboard versions
main_url = 'https://www.keychron.com/collections/all'

# Fetch the main page content
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product links
product_links = []
for a_tag in soup.find_all('a', href=True):
    if '/products/' in a_tag['href']:
        product_links.append('https://www.keychron.com' + a_tag['href'])

# Remove duplicates
product_links = list(set(product_links))

# Print all the product URLs
for link in product_links:
    print(link)