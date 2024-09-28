import re
import aiohttp
from bs4 import BeautifulSoup
import asyncio
from datetime import datetime

async def fetch_html(url, session, headers):
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Failed to retrieve the page. Status code: {response.status}")
            return None

async def post_comment(url, session, headers, data):
    async with session.post(url, headers=headers, data=data) as response:
        return response.status, await response.text()

async def wait_until_target_time(target_time):
    """Keep waiting until the current time matches the target_time (11:00 PM)."""
    while True:
        now = datetime.now()
        current_time_str = now.strftime("%H:%M:%S")
        print(f"Current time: {current_time_str}. Waiting for {target_time}.")
        
        if current_time_str == target_time:
            print(f"Reached {target_time}. Proceeding to post comment.")
            break
        
        await asyncio.sleep(1)  # Sleep for 30 seconds before checking the time again

async def main():
    increment = 10
    url = "https://mbasic.facebook.com/groups/1084600079916206/permalink/1084637039912510"
    comment_url = "https://mbasic.facebook.com/a/comment.php?fs=8&fr=%2Fwap%2Fprofile_tribe.php&actionsource=0&comment_logging&ft_ent_identifier=1084637039912510&eav=AfY-EV63qxaiiG4nDQWOyjBIDnM8o-IOxxCQvaFqAT8-6Z2RH6pHcIQMrBXUY0QF1c4&av=100024534830806&gfid=AQD0W8XmFaydssodbws&paipv=0&refid=18"
    cookie = 'sb=5-bKZg1MeeTsf36ddkSqjGDi; datr=5-bKZk2mUtAMf4xybb4bbx9d; c_user=100024534830806; ps_l=1; ps_n=1; m_page_voice=100024534830806; wd=1271x652; presence=C%7B%22lm3%22%3A%22sc.8030610987047451%22%2C%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22sc.7244691427493896254%22%7D%5D%2C%22utc3%22%3A1727269043362%2C%22v%22%3A1%7D; fr=1J9wM1kVncMtd3cVu.AWV7xsqsxENq28n-xJiFeafGoU8.Bm9Blk..AAA.0.0.Bm9Blk.AWVG698f0fw; xs=7%3A4wXbuMlt8eLAwQ%3A2%3A1724573435%3A-1%3A6297%3A%3AAcUij1gy04T_79a677Dd0Mg-NNgRdnkPPRy-dZ7ZhuA; datr=gR70ZuIIZmNguO5jNR6x_jCP; fr=0aYonQxsu8Oqt5qa5..Bm9B6C..AAA.0.0.Bm9B6C.AWUiGm7Ws-Y; sb=gh70ZjgsxpluV6tBdppl_Pq9'
    headers = {
        'cookie': cookie,
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    target_time = input("HH:MM:SS: ")  # 11:00 PM in 24-hour format

    async with aiohttp.ClientSession() as session:
        await wait_until_target_time(target_time)  # Wait until the predefined time
        
        html_content = await fetch_html(url, session, headers)
        if html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser')
        comment_elements = soup.find_all('div', class_='do')

        import re

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
            payload = f'fb_dtsg=NAcPq_04MjDsfkRHa0tinSqUel84oZ_ONYbfd4GeXFWxk_dIzDzJuOw%3A7%3A1724573435&jazoest=25632&comment_text={comment_text}'
            post_headers = headers.copy()
            post_headers.update({
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mbasic.facebook.com',
                'sec-fetch-site': 'same-origin'
            })
            status, response_text = await post_comment(comment_url, session, post_headers, payload)
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

# Run the async main function
asyncio.run(main())
