# Instagram DM Monitor & Telegram Alert Bot

## Overview
This project is a Python-based automation tool that monitors Instagram Direct Messages for a specific keyword and sends an alert to a Telegram group when that keyword is detected. It utilizes Selenium for web automation, Tesseract OCR for text extraction from images, and Telethon & python-telegram-bot for Telegram messaging.

## Features
- Logs into Instagram automatically.
- Monitors the latest Direct Messages for specific keywords.
- Extracts text from Instagram using OCR (Tesseract).
- Sends an emergency alert to a specified Telegram group when the keyword is detected.

## Prerequisites
Before running the script, ensure you have the following installed and configured:

### 1. Install Dependencies
Install the required Python libraries:
```bash
pip install selenium pillow pytesseract telethon python-telegram-bot
```

### 2. Install Tesseract OCR
- Download and install Tesseract OCR from [Tesseract's official site](https://github.com/UB-Mannheim/tesseract/wiki).
- After installation, configure the path to the executable in the script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
  ```

### 3. Set Up Selenium WebDriver
- Download ChromeDriver from [ChromeDriver official site](https://sites.google.com/chromium.org/driver/).
- Extract the downloaded file and note its path.
- Update the `path` variable in the script:
  ```python
  path = "C:/path/to/chromedriver.exe"
  ```

### 4. Get Telegram API Credentials
- Create a Telegram API ID and Hash Key from [my.telegram.org](https://my.telegram.org/).
- Add these to the script:
  ```python
  API_ID = YOUR_API_ID
  API_HASH = "YOUR_API_HASH"
  ```

### 5. Get Telegram Bot Token
- Create a Telegram bot via [BotFather](https://t.me/BotFather) and obtain a token.
- Update the script:
  ```python
  Bot_token = "YOUR_BOT_TOKEN"
  ```

### 6. Get Telegram Group Chat ID
To obtain your Telegram group chat ID, run the following script:
```python
from telethon.sync import TelegramClient

API_ID = YOUR_API_ID
API_HASH = "YOUR_API_HASH"
Phone_number = "YOUR_PHONE_NUMBER"
SESSION_FILE = "insta/Session_telegram.session"

client = TelegramClient(SESSION_FILE, API_ID, API_HASH)

async def main():
    await client.start()
    async for dialog in client.iter_dialogs():
        print(f"Chat: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
```
- Find your group name in the output and note the corresponding ID.
- Update the script:
  ```python
  GROUP_CHAT_ID = YOUR_GROUP_CHAT_ID
  ```

## Usage
1. Update the script with your Instagram credentials:
   ```python
   username = "your_instagram_username"
   password = "your_instagram_password"
   ```
2. Run the script:
   ```bash
   python script.py
   ```
3. The script will:
   - Log into Instagram.
   - Monitor the latest DM.
   - Extract text using OCR.
   - Send an alert to the Telegram group if the keyword is detected.

## Important Notes
- The bot sends an emergency alert when the keyword **"knock"** is detected.
- To stop the script, send the word **"end"** in the monitored chat.
- Ensure your bot is added to the Telegram group where you want alerts to be sent.
- Your Instagram credentials and Telegram API details should be kept secure.

## Disclaimer
This script automates interactions with Instagram, which may violate its Terms of Service. Use at your own risk.

