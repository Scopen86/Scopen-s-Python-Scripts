from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 


driver = webdriver.Chrome()
driver.get(f"https://khoahoc.vietjack.com/question/106622/mot-quan-the-dang-o-trang-thai-can-bang-di-truyen-co-tan-so-alen-a-0-6")

time.sleep(3)

correct_ans = driver.find_element(By.CSS_SELECTOR, "[data-answer-value='Y']")
ans_id = correct_ans.get_attribute("id")
print(ans_id)

ans_value = driver.find_element(By.XPATH, f'//*[@id="{ans_id}"]/label/p/span').text
print(ans_value)

input()





