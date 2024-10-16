from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 
from difflib import SequenceMatcher
import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"




def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


username = "0358659304"
password = "123456789"
question_num = 40
exam_code = "bak9il"

#0 for False / 1 for True
random_element = 0

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(f"https://sogddtthanhhoa.azota.vn/vi/auth/login?return_url=%2Fvi%2Fde-thi%2F{exam_code}&from=register&user_click=true")

#driver.get(f"https://azota.vn/vi/auth/login?return_url=%2Fvi%2Fde-thi%2F{exam_code}&from=register&user_click=true")

time.sleep(3)

"""username_box = driver.find_element(By.XPATH, '//*[@id="homework-layout"]/app-login/auth-layout/div[1]/div/div/div[2]/div/div/div/form/div[1]/div[1]/input')
password_box = driver.find_element(By.XPATH, '//*[@id="homework-layout"]/app-login/auth-layout/div[1]/div/div/div[2]/div/div/div/form/div[1]/div[2]/div/input')


username_box.send_keys(username)
password_box.send_keys(password)
password_box.send_keys(Keys.RETURN)
time.sleep(5)

start_btn = driver.find_element(By.XPATH, '//*[@id="azt-layout"]/div[1]/div[2]/div/div[2]/azt-parent-checking-box/div/div/div/div[3]/button')
start_btn.click()

time.sleep(4)
#layout_btn = driver.find_element(By.XPATH, '/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-take-test/div/div/div[1]/div[5]/button')
#layout_btn.click()
time.sleep(2)"""
input()


def search(search_query):

    options = ChromeOptions()
    options.add_argument("--headless=new")

    search_driver = webdriver.Chrome(options=options)
    # Navigate to Google's homepage
    search_driver.get("https://www.google.com")

    # Find the search bar element and type your query
    search_box = search_driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)

    # Press 'Enter' to perform the search
    try:
        search_box.send_keys(Keys.RETURN)
    except Exception: pass
    time.sleep(3)

    first_result = search_driver.find_element(By.CLASS_NAME, 'CA5RN')
    first_result.click()
    # Wait for the search results to load
    time.sleep(3)  # You can adjust the wait time based on your internet speed

    correct_ans = search_driver.find_element(By.CSS_SELECTOR, "[data-answer-value='Y']")
    ans_id = correct_ans.get_attribute("id")
    print(ans_id)

    ans_value = search_driver.find_element(By.XPATH, f'//*[@id="{ans_id}"]/label').text
    print(ans_value)

    return ans_value





for i in range(question_num):
    #try:/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-coazt-take-test/div/div/div/div/div[{i + 2 + random_element}]/div/azt-question-standalone-for-student-at-full-test/div/div/div[1]
    #base_renderer = driver.find_element(By.XPATH, f'/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-take-test/div/div/div[2]/div[{i + 2 + random_element}]/div/azt-question-standalone-for-student-at-full-test/div/div/div[1]')
    base_renderer = driver.find_element(By.XPATH, f'/html/body/app-root/azota-load-env-error-box/azota-business-package-expired-box/div/mat-drawer-container/mat-drawer-content/app-test-dashboard/div/app-coazt-take-test/div/div/div/div/div[{i + 2 + random_element}]/div/azt-question-standalone-for-student-at-full-test/div/div/div[1]')
    renderer_id = base_renderer.get_attribute("id")
    id = renderer_id.strip("question_render_container_")

    question_elem = driver.find_element(By.XPATH, f'//*[@id="question_render_container_{id}"]/div/div[2]/azt-dynamic-hook')
    question = question_elem.text


    ansA = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[1]/div/azt-dynamic-hook').text
    ansB = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[2]/div/azt-dynamic-hook').text
    ansC = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[3]/div/azt-dynamic-hook').text
    ansD = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[4]/div/azt-dynamic-hook').text


    ansA_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[1]/button')
    ansB_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[2]/button')
    ansC_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[3]/button')
    ansD_btn = driver.find_element(By.XPATH, f'//*[@id="question_render_element_{id}"]/div/div[2]/azt-question-answer-view-for-student-at-step-page/div[2]/div/div[4]/button')

    try: 
        corect_ans = search(f'site:khoahoc.vietjack.com {question}, {ansA}, {ansB}, {ansC}, {ansD}')
    except Exception: corect_ans = "Found. Nonee"
    try:
        temp, final_ans = corect_ans.split(". ", 1)
    except Exception: final_ans = corect_ans
    final_ans = final_ans.strip()

    print(repr(id))
    print(repr(question))
    print(repr(ansA), repr(ansB), repr(ansC), repr(ansD))

    A_similarity = similar(final_ans, ansA)
    B_similarity = similar(final_ans, ansB)
    C_similarity = similar(final_ans, ansC)
    D_similarity = similar(final_ans, ansD)

    similarity_dict = {'A': A_similarity, 'B': B_similarity, 'C': C_similarity, 'D': D_similarity}
    max_var = max(similarity_dict, key=similarity_dict.get)
    max_value = max(similarity_dict.values())

    if max_value < 0.5:

        client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"{question}, {ansA}, {ansB}, {ansC}, {ansD}. Please answer briefly without explanation",
                }
            ],
            model="llama3-8b-8192",
        )

        chat_response = chat_completion.choices[0].message.content
        final_ans = chat_response
        print(chat_response)
        time.sleep(5)


        A_similarity = similar(final_ans, ansA)
        B_similarity = similar(final_ans, ansB)
        C_similarity = similar(final_ans, ansC)
        D_similarity = similar(final_ans, ansD)

        similarity_dict = {'A': A_similarity, 'B': B_similarity, 'C': C_similarity, 'D': D_similarity}
        max_var = max(similarity_dict, key=similarity_dict.get)


    print(max_var)
    print(repr(final_ans))
    if max_var == "A": ansA_btn.click()
    if max_var == "B": ansB_btn.click()
    if max_var == "C": ansC_btn.click()
    if max_var == "D": ansD_btn.click()


    



    try:
        next_question_btn = driver.find_element(By.XPATH, f"""//*[@id="container-content"]/div[2]/div[{42 + random_element}]/div/div[{i+2}]/button""")
        next_question_btn.click()
    except Exception: pass

    

input()


