from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 


driver = webdriver.Chrome()

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search bar element and type your query
search_box = driver.find_element(By.NAME, "q")
search_query = """site:khoahoc.vietjack.com Gen A nằm trên nhiễm sắc thể thưòng có 10 alen. Biết không xảy ra đột biến. Theo lí thuyết, có bao nhiêu phát biểu sau đây đúng:
I. Quần thể có tối đa 55 kiểu gen.
II. Quần thể có tối đa 10 loại giao tử đực.
III. Quần thể có tối đa 10 kiểu gen đồng hợp.
IV. Quần thể có tối đa 45 kiểu gen dị hợp tử.: Đáp án A.: 3 ; Đáp án B.: 2 ; Đáp án C.: 1 ; Đáp án D.: 4. """
search_box.send_keys(search_query)

# Press 'Enter' to perform the search
try:
    search_box.send_keys(Keys.RETURN)
except Exception: pass

first_result = driver.find_element(By.CLASS_NAME, 'iUh30')
first_result.click()
# Wait for the search results to load
time.sleep(3)  # You can adjust the wait time based on your internet speed

input()
