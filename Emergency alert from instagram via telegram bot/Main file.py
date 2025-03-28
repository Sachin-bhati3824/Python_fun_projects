import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from PIL import Image
import pytesseract
import os 
from telethon import TelegramClient
from telegram import Bot

def extract_text():
    screenshot_path  = "full_screesnhot.png"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    driver.save_screenshot(screenshot_path)
    x,y,width,height = 650, 596,350,130
    image = Image.open(screenshot_path)
    cropped_image = image.crop((x,y,x+width,y+height))
    cropped_image_path = "cropped.png"
    cropped_image.save(cropped_image_path)
    extract = pytesseract.image_to_string(cropped_image)
    return extract 
    os.remove(screenshot_path)
    os.remove(cropped_image_path)


def send_the_alert():
    API_ID = 
    API_HASH = ""
    Phone_number = "+"
    SESSION_FILE = "insta/Session_telegram.session"
    GROUP_CHAT_ID =   # Replace with actual Group ID
    Bot_token = ""
    bot = Bot(token=Bot_token)
    # To obtain the bot token just go to the BotFather on the telegram and then type /newbot 
    # and follow some easy steps then you will get your Bot token 

    
    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
    async def main():
        await client.start(Phone_number)
        await client.send_message("me", "emer")
        await client.send_message(GROUP_CHAT_ID, "🚨 Emergency Alert! @all")  # Sends to your Saved Messages
        await bot.send_message(GROUP_CHAT_ID, "🚨 Emergency Alert! Please check immediately! 🚨")

    with client:
        client.loop.run_until_complete(main())



username = ""
password = ""
url = 'https://www.instagram.com'

path = "C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]').send_keys(username)
driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button').click()
genres_list_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label*="Messenger"]')))
    
genres_list_1.click()
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
not_now.click()
time.sleep(4)
sunno = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')))
sunno.click()
actions = ActionChains(driver)
for i in range(2):
    actions.move_by_offset(100,150).click().perform()
    time.sleep(1)
last_message_i = '' 
text_list = ['_'] 
while True:
    time.sleep(2)
    last_message_i = text_list[-1] if text_list else ''
    text_list = [] 
    text = extract_text()
    text_list = text.split()
    last_message = text_list[-1] if text_list else '' 
    if last_message != last_message_i:
        if last_message == "knock" or last_message == "Knock":
            send_the_alert()
        
    if 'end' in text_list :
        break   


driver.quit()
#use the following code to obtain the Group chat ID , just run this and find the name of your group and just in front of it you will find your group chat ID 
# from telethon.sync import TelegramClient

# # Replace these with your details

# API_ID = 
# API_HASH = ""
# Phone_number = "+"
# SESSION_FILE = "insta/Session_telegram.session"

# client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

# async def main():
#     await client.start()
#     async for dialog in client.iter_dialogs():
#         print(f"Chat: {dialog.name}, ID: {dialog.id}")

# with client:
#     client.loop.run_until_complete(main())


#after making the bot add it to a group which group chat ID you have fetched with the above commented code then you will get the message of that bot in the following group 
