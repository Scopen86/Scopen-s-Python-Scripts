import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_html(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def post_comment(url, headers, data):
    response = requests.request("POST", url, headers=headers, data=data)
    return response.status_code, response.text

def wait_until_target_time(target_time):
    """Keep waiting until the current time matches the target_time."""
    while True:
        now = datetime.now()
        current_time_str = now.strftime("%H:%M:%S")
        print(f"Current time: {current_time_str}. Waiting for {target_time}.")
        
        if current_time_str == target_time:
            print(f"Reached {target_time}. Proceeding to post comment.")
            break
        
        time.sleep(1)  # Sleep for 1 second before checking the time again

def main():
    increment = 10
    url = "https://mbasic.facebook.com/groups/379083037835147/permalink/568396942237088"
    comment_url = "https://mbasic.facebook.com/a/comment.php?fs=8&fr=%2Fwap%2Fprofile_tribe.php&actionsource=0&comment_logging&ft_ent_identifier=568396942237088&eav=AfbCraGzLW6cqGUGmmt2p7m5tBQlxVcgpYSA0DBsR1yNEzFEtiKrLNSQTrpYoicgxyU&av=100024534830806&gfid=AQDJNEOghIj7_iiE6AY&paipv=0&refid=18"
    cookie = 'sb=Q4cDZ3WX1H50RUzpZMPOQWDW; ps_l=1; ps_n=1; datr=RIcDZ0KEQRMD5pIu1Ky7dVqu; c_user=100024534830806; wd=1209x692; xs=39%3AZrUlfsvEwWnV7w%3A2%3A1728284488%3A-1%3A6297%3A%3AAcXcuC01hG3NLf9AHHPruOF4ylrmLJnPlsCobCA_bA; m_page_voice=100024534830806; fr=1nUNco2KB97r1CQYF.AWUBo07hY3LtwifHivJ73q-AihA.BnBLNx..AAA.0.0.BnBLuG.AWX5yK14yE0; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728363436193%2C%22v%22%3A1%7D; c_user=100024534830806; datr=RIcDZ0KEQRMD5pIu1Ky7dVqu; fr=15Fa1Ml09v3AXx5T5.AWXjhEW-v7rLfkE6EJHxUjZ_wfI.BnBMzt..AAA.0.0.BnBMzt.AWXUaEn-5kI; xs=39%3AZrUlfsvEwWnV7w%3A2%3A1728284488%3A-1%3A6297%3A%3AAcXqlZ-uRRgOJJ-J4Y2aJB-40uinv9VL-p8qIivYSg'
    headers = {
        'cookie': cookie,
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    target_time = input("HH:MM:SS: ")  # 11:00 PM in 24-hour format

    wait_until_target_time(target_time)  # Wait until the predefined time
    
    html_content = fetch_html(url, headers)
    if html_content is None:
        return

    soup = BeautifulSoup(html_content, 'html.parser')
    comment_elements = soup.find_all('div', class_='ek')

    largest_number = None
    comment_with_largest_number = None

    for comment in comment_elements:
        comment_text = comment.text.strip()
        
        # Find all sequences of digits, periods, or commas
        numbers = re.findall(r'\d+[.,]?\d*', comment_text)
        
        if numbers:
            # Clean numbers by removing commas/periods and converting to integers
            cleaned_numbers = [int(re.sub(r'[.,]', '', number)) for number in numbers]
            
            max_number_in_comment = max(cleaned_numbers)
            if largest_number is None or max_number_in_comment > largest_number:
                largest_number = max_number_in_comment
                comment_with_largest_number = comment_text

    if comment_with_largest_number:
        print(f"Comment with the largest number: {comment_with_largest_number}")
        print(f"Largest number found: {largest_number}")

        comment_text = str(largest_number + increment * 2)
        payload = f'fb_dtsg=NAcNLwxrkQ8-K-pV4jjWbs9ZNrFZh_-Q5fpER2Y56RNaQbaXnFy9NnA%3A39%3A1728284488&jazoest=25396&comment_text={comment_text}'
        post_headers = headers.copy()
        post_headers.update({
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        status, response_text = post_comment(comment_url, post_headers, payload)
        print(f"Response Status: {status}")
        #print(f"Response Text: {response_text}")  # Print response for debugging
        if status in (200, 302):
            now = datetime.now()
            current_time_str = now.strftime("%H:%M:%S")
            print(f"Commented: {comment_text} at {current_time_str}")
        else:
            print(f"Failed to comment. Status code: {status}")
    else:
        print("No comments with numbers found.")

# Run the main function
if __name__ == "__main__":
    main()