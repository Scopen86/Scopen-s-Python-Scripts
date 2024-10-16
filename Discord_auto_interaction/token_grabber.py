from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from PIL import Image
import io
import time

from terminal_qr_code import decode_and_display_qr_code

def grab_discord_token():
    # Set up Edge options
    edge_options = Options()
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Initialize the WebDriver
    driver = webdriver.Edge(options=edge_options)

    # Navigate to Discord login page
    driver.get("https://discord.com/login")

    # Wait for the QR code SVG element to be present
    try:
        qr_code_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.qrCode_c6cd4b"))
        )
        
        print("QR code SVG element found.")
    except TimeoutException:
        print("Timed out waiting for QR code SVG element to appear.")
        driver.quit()
        return None

    # Find the element you want to screenshot
    element = driver.find_element(By.CSS_SELECTOR, "div.qrCode_c6cd4b")

    # Capture the screenshot of the entire page
    screenshot = driver.get_screenshot_as_png()

    # Get the location and size of the element
    location = element.location
    size = element.size

    # Open the screenshot using PIL
    image = Image.open(io.BytesIO(screenshot))

    # Calculate the boundaries of the element
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # Crop the image to the element's dimensions
    element_image = image.crop((left, top, right, bottom))

    decode_and_display_qr_code(element_image)

    # Attempt to grab the token from local storage after login
    t_end = time.time() + 60 * 2
    while time.time() < t_end:
        discord_login = driver.current_url
        if discord_login != 'https://discord.com/login':
            print('Grabbing token... \n')
            token = driver.execute_script('''
                window.dispatchEvent(new Event('beforeunload'));
                let iframe = document.createElement('iframe');
                iframe.style.display = 'none';
                document.body.appendChild(iframe);
                let localStorage = iframe.contentWindow.localStorage;
                var token = JSON.parse(localStorage.token);
                return token;
            ''')
            print('------------------------------------------------------------------------------------------')
            print('Token grabbed:', token)
            print('------------------------------------------------------------------------------------------')
            driver.quit()
            return token

    driver.quit()
