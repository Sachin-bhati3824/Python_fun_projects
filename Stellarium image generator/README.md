# 🌌 SkyBot – Night Sky & Moon Image Generator

SkyBot is a professional-grade astronomy tool built with Django and Python that uses [Stellarium](https://stellarium.org/) to generate stunning images of the moon and night sky based on a specific date and time.

Users can interact via:
- A REST API (`/api/generate/`)
- A Telegram bot (`@YourBotUsername`)

---

## ✨ Features

- 📅 Generate historical or future sky/moon images by date
- 🕗 Customizable observation time (default: 8:00 PM)
- 🛰️ Accurate celestial rendering using Stellarium
- 🗺️ Configured for New Delhi (can be changed)
- 📷 Screenshots are generated and auto-sent by Telegram
- ⚙️ Runs locally using Windows with `.ssc` script automation

---

## 🖼️ Example

A user sends:
/sky 2025-12-31 21:00:00


Bot responds with:
- 🌕 An image of the moon as it appeared that night
- 🌌 A wide-angle view of the night sky from New Delhi

---

## 🛠️ Tech Stack

| Component     | Technology                |
|---------------|----------------------------|
| Backend       | Django + Django REST API   |
| Astronomy     | [Stellarium (CLI)](https://stellarium.org/) |
| Telegram Bot  | python-telegram-bot v20+   |
| Scripts       | `.ssc` files               |
| OS            | Windows (tested on Win 11) |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/skybot.git
cd skybot
```


### 2. Set Up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```
### 3. Configure Stellarium

Install Stellarium on your system

In Stellarium, disable UI elements and set screenshot path to output/

Make sure Stellarium is accessible via CLI:

```bash
stellarium.exe --startup-script=scripts/moon.ssc
```
### 4. Start the Django Server
```bash
python manage.py runserver
```
### 5. Run the Telegram Bot

```bash
python bot/bot.py
```
## 🔗 API Usage
Endpoint:

```bash
POST /api/generate/
```

Payload:

```bash
{
  "date": "2025-12-31",
  "time": "21:00:00"
}
```
Response:

```bash
{
  "moon_image": "D:/Stellarium project/output/moon.png",
  "sky_image": "D:/Stellarium project/output/sky.png"
}
```
# 📁 Project Structure
```bash
skybot/
├── api/                 # Django app
│   ├── views.py
│   ├── run_stellarium.py
│   ├── ssc_generator.py
├── bot/
│   └── bot.py           # Telegram bot
├── scripts/             # Generated .ssc scripts
├── output/              # Output images (moon.png, sky.png)
├── manage.py
├── requirements.txt
└── README.md
```
### ⚠️ Notes 

Ensure stellarium.exe is correctly linked in run_stellarium.py

This project currently uses fixed location coordinates (New Delhi). Can be expanded for dynamic input.

Telegram bots have a 10-second response timeout. This project uses asyncio.create_task(...) to handle that.


# 👨‍💻 Author

Made with ❤️ by Sachin Bhati


GitHub: https://github.com/Sachin-bhati3824