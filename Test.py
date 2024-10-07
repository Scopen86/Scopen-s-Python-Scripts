import json
import urllib.request

from bs4 import BeautifulSoup

URL = ("https://www.keychron.com/products/keychron-k6-wireless-mechanical-keyboard")
oururl= urllib.request.urlopen(URL).read()
soup = BeautifulSoup(oururl)


# Parse the JSON data
product_data = json.loads(soup.find('script', type='application/ld+json').text)

# Extract and print SKU and name for each offer
for offer in product_data["offers"]:
  sku = offer.get("sku")
  name = offer.get("name")
  if sku and name:
    print(f"SKU: {sku}, Name: {name}")
