from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 
from g4f.client import Client

username = "0358659304"
password = "123456789"
question_num = 40
exam_code = "jyiup8"

driver = webdriver.Chrome()
driver.get(f"https://azota.vn/vi/auth/login?return_url=%2Fvi%2Fde-thi%2F{exam_code}&from=register&user_click=true")

time.sleep(3)

username_box = driver.find_element(By.XPATH, '//*[@id="homework-layout"]/app-login/auth-layout/div[1]/div/div/div[2]/div/div/div/form/div[1]/div[1]/input')
password_box = driver.find_element(By.XPATH, '//*[@id="homework-layout"]/app-login/auth-layout/div[1]/div/div/div[2]/div/div/div/form/div[1]/div[2]/div/input')


username_box.send_keys(username)
password_box.send_keys(password)
password_box.send_keys(Keys.RETURN)
time.sleep(2)

#start = driver.find_element(By.XPATH, '/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-student-view/student-layout/div/div[1]/div[2]/div/div[2]/azt-parent-checking-box/div/div/div/div[3]/button')
#start.click()
#actions = ActionChains(driver)
#actions = actions.send_keys(Keys.TAB)
#actions = actions.send_keys(Keys.TAB)
#actions = actions.send_keys(Keys.RETURN)
#actions.perform()
input()

time.sleep(4)

layout_btn = driver.find_element(By.XPATH, '/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-take-test/div/div/div[1]/div[5]/button')
layout_btn.click()
time.sleep(2)

first_ques_elem = driver.find_element(By.XPATH, '/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-take-test/div/div/div[2]/div[2]/div/azt-question-standalone-for-student-at-full-test/div')
first_id = first_ques_elem.get_attribute("id")
base_id = first_id.strip("question_render_element_")
print(base_id)


for id in range(int(base_id) , int(base_id) + question_num):
    try:
        question_elem_xpath = f'//*[@id="question_render_container_{id}"]/div/div[2]/azt-dynamic-hook/span'
        question_elem = driver.find_element(By.XPATH, question_elem_xpath)
        question = question_elem.text
        print(question)

        ansA = driver.find_element(By.XPATH, f'//*[@id="question_render_container_{id}"]/div/div[3]/div[1]').text
        ansB = driver.find_element(By.XPATH, f'//*[@id="question_render_container_{id}"]/div/div[3]/div[2]').text
        ansC = driver.find_element(By.XPATH, f'//*[@id="question_render_container_{id}"]/div/div[3]/div[3]').text
        ansD = driver.find_element(By.XPATH, f'//*[@id="question_render_container_{id}"]/div/div[3]/div[4]').text
        print(ansA, ansB, ansC, ansD)

        client = Client()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"{question}: Đáp án A.: {ansA} ; Đáp án B.: {ansB} ; Đáp án C.: {ansC} ; Đáp án D.: {ansD}, chỉ trả lời bằng đáp án A., B., C. hoặc D. "}] 
        )
        
        final_ans = response.choices[0].message.content
        print(final_ans)

        ansA_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[1]/div[2]/button[1]')
        ansB_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[1]/div[2]/button[2]')
        ansC_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[1]/div[2]/button[3]')
        ansD_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[1]/div[2]/button[4]')

        if "A." in final_ans : ansA_btn.click()
        if "B." in final_ans : ansB_btn.click()
        if "C." in final_ans : ansC_btn.click()
        if "D." in final_ans : ansD_btn.click()

        next_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[2]/a')
        next_btn.click()
    except Exception:
        try:
            next_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/div/div[2]/a')
            next_btn.click()
        except Exception: pass

    

input()