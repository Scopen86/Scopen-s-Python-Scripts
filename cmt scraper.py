import re
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content using the provided headers and URL
url = "https://mbasic.facebook.com/groups/1084600079916206/permalink/1084637039912510"
comment_url = "https://mbasic.facebook.com/a/comment.php?fs=8&fr=%2Fwap%2Fprofile_tribe.php&actionsource=0&comment_logging&ft_ent_identifier=1084637039912510&eav=AfY-EV63qxaiiG4nDQWOyjBIDnM8o-IOxxCQvaFqAT8-6Z2RH6pHcIQMrBXUY0QF1c4&av=100024534830806&gfid=AQD0W8XmFaydssodbws&paipv=0&refid=18"

cookie = 'sb=5-bKZg1MeeTsf36ddkSqjGDi; datr=5-bKZk2mUtAMf4xybb4bbx9d; c_user=100024534830806; ps_l=1; ps_n=1; m_page_voice=100024534830806; wd=1271x652; presence=C%7B%22lm3%22%3A%22sc.8030610987047451%22%2C%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22sc.7244691427493896254%22%7D%5D%2C%22utc3%22%3A1727269043362%2C%22v%22%3A1%7D; fr=1J9wM1kVncMtd3cVu.AWV7xsqsxENq28n-xJiFeafGoU8.Bm9Blk..AAA.0.0.Bm9Blk.AWVG698f0fw; xs=7%3A4wXbuMlt8eLAwQ%3A2%3A1724573435%3A-1%3A6297%3A%3AAcUij1gy04T_79a677Dd0Mg-NNgRdnkPPRy-dZ7ZhuA; datr=gR70ZuIIZmNguO5jNR6x_jCP; fr=0aYonQxsu8Oqt5qa5..Bm9B6C..AAA.0.0.Bm9B6C.AWUiGm7Ws-Y; sb=gh70ZjgsxpluV6tBdppl_Pq9'
increment = 10


payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': cookie,
  'dpr': '1',
  'priority': 'u=0, i',
  'sec-ch-prefers-color-scheme': 'dark',
  'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-full-version-list': '"Microsoft Edge";v="129.0.2792.52", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.59"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
  'viewport-width': '716'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract the comments (assuming comments are inside div elements with the class 'do')
comments = []
comment_elements = soup.find_all('div', class_='do')

# Initialize variables to store the comment with the largest number and the largest number itself
largest_number = None
comment_with_largest_number = None

# Step 4: Iterate through comments and find the one with the largest number
for comment in comment_elements:
    comment_text = comment.text.strip()
    
    # Find all numbers in the comment using regex
    numbers = re.findall(r'\d+', comment_text)
    
    if numbers:
        # Convert the found numbers to integers
        numbers = list(map(int, numbers))
        
        # Get the largest number in the current comment
        max_number_in_comment = max(numbers)
        
        # Compare with the largest number we've seen so far
        if largest_number is None or max_number_in_comment > largest_number:
            largest_number = max_number_in_comment
            comment_with_largest_number = comment_text

# Step 5: Print the comment with the largest number
if comment_with_largest_number:
    print(f"Comment with the largest number: {comment_with_largest_number}")
    print(f"Largest number found: {largest_number}")
else:
    print("No comments with numbers found.")



comment_text = largest_number + increment * 2
payload = f'fb_dtsg=NAcPq_04MjDsfkRHa0tinSqUel84oZ_ONYbfd4GeXFWxk_dIzDzJuOw%3A7%3A1724573435&jazoest=25632&comment_text={comment_text}'
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': cookie,
  'dpr': '1',
  'origin': 'https://mbasic.facebook.com',
  'priority': 'u=0, i',
  'referer': 'https://mbasic.facebook.com/groups/1084600079916206/permalink/1084600966582784/?paipv=0&eav=AfYGSBJFacQOqniS7oOi9Ggj7eMsZ8UDgbcvPHBkRgNhfpNsJx-Lu_NawykHjfPDEP0&_rdr',
  'sec-ch-prefers-color-scheme': 'dark',
  'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-full-version-list': '"Microsoft Edge";v="129.0.2792.52", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.59"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
  'viewport-width': '716'
}

response = requests.request("POST", comment_url, headers=headers, data=payload)


# Check if the request was successful
if response.status_code == 200 or response.status_code == 302:
    print(f"Commented: {comment_text}")
else:
    print(f"Failed to comment. Status code: {response.status_code}")
    exit()
