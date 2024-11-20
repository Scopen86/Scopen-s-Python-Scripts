import requests
import json
from bs4 import BeautifulSoup

# URL of the main page containing the keyboard versions
main_url = 'https://www.keychron.com/collections/all'

# Fetch the main page content
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product links
product_links = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if '/products/' in href:
        if not href.startswith('http'):
            href = 'https://www.keychron.com' + href
        product_links.append(href)

# Remove duplicates
product_links = list(set(product_links))

# Open the output file
with open('output.txt', 'w') as file:
    # Function to extract SKU and options from a product page
    def extract_sku_options(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag containing the product data
        for script in soup.find_all('script'):
            if 'var meta' in script.text:
                json_text = script.text.strip().split('var meta =', 1)[1].strip(' ;')
                json_text = json_text.split('};', 1)[0] + '}'  # Extract only the JSON part
                try:
                    product_data = json.loads(json_text)
                    # Extract SKU and options
                    for variant in product_data['product']['variants']:
                        sku = variant['sku']
                        options = variant.get('public_title', '')
                        output_line = f"{sku} - {options}\n"
                        file.write(output_line)
                        print(output_line, end='')  # end='' prevents double newlines
                except json.JSONDecodeError as e:
                    error_msg = f"JSON decode error: {e}\n"
                    file.write(error_msg)
                    print(error_msg, end='')
                break

    # Iterate over all product links and extract SKU and options
    for link in product_links:
        status_msg = f"Processing URL: {link}\n"
        file.write(status_msg)
        print(status_msg, end='')
        extract_sku_options(link)