from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import base64

# Load group links and content
with open('group_link.txt', 'r', encoding='utf-8') as f:
    group_links = f.read().splitlines()

with open('content.txt', 'r', encoding='utf-8') as f:
    post_content = f.read()

# Initialize the Edge WebDriver
driver = webdriver.Edge()  # Make sure to have the appropriate Edge WebDriver installed

# Login to Facebook
driver.get("https://www.facebook.com/")
time.sleep(2)  # Wait for the page to load

# Enter email and password
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("quy3501")  # Replace with your email

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys("Sc0pe86_meta")  # Replace with your password

# Click the login button
login_button = driver.find_element(By.NAME, "login")
login_button.click()
time.sleep(5)  # Wait for the login process to complete

# Loop through each group link
for index, group_link in enumerate(group_links):
    driver.get(group_link)
    time.sleep(5)  # Wait for the page to load

    # Find the post input area using the parent div of the placeholder text
    post_placeholder = driver.find_element(By.XPATH, "//span[contains(text(), 'Bạn viết gì đi...')]/parent::div")
    post_placeholder.click()  # Click on the parent div first
    time.sleep(2)  # Wait for the post area to load
    post_area = driver.find_element(By.XPATH, "//div[@aria-label='Bạn viết gì đi...' and @contenteditable='true']")  # Find the post area using the new criteria
    post_area.send_keys(post_content)

    # Attach the image
    image_path = f"{index + 1}.img"  # Assuming images are named 1.img, 2.img, etc.
    image_path = os.path.abspath(image_path)
    print(image_path)
    if (image_path):
        print(f"Uploading image: {image_path}")

        image_button = driver.find_element(By.XPATH, "//div[@aria-label='Ảnh/video' and @role='button']")
        image_button.click()

        # Load your file in binary mode and encode it as base64
        with open(image_path, "rb") as f:
            file_content = base64.b64encode(f.read()).decode()

        # Locate the drag-and-drop area (replace with your actual locator)
        drop_area = driver.find_element("xpath", "//div[@id='drag-drop-area']")

        # JavaScript code to simulate drag-and-drop event
        js_script = """
        var dataTransfer = new DataTransfer();
        dataTransfer.items.add(new File([Uint8Array.from(atob(arguments[0]), c => c.charCodeAt(0))], 'filename.txt'));
        var dropEvent = new DragEvent('drop', { dataTransfer });
        arguments[1].dispatchEvent(dropEvent);
        """

        # Execute the script with file content and drop area element
        driver.execute_script(js_script, file_content, drop_area)
        # file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"][accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
        # file_input.send_keys(image_path)
        time.sleep(2)  # Wait for the image to upload

    # Post the content
    post_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Đăng')]/parent::div")
    time.sleep(5)  # Wait for the post to be submitted

input("Press Enter to exit...")

# Close the WebDriver
driver.quit()

