import asyncio
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "your telgram bot token "  
DJANGO_API_URL = "http://localhost:8000/api/generate/"
DEFAULT_TIME = "20:00:00"

# Called when user types /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SkyBot! \nUse: /sky YYYY-MM-DD [HH:MM:SS]\n\nExamples:\n"
        "/sky 2025-12-31\n/sky 2025-12-31 21:30:00"
    )

# Separates the heavy logic
async def send_images(update: Update, context: ContextTypes.DEFAULT_TYPE, date: str, time: str):
    
    result = call_django_api(date, time)
    if not result:
        await update.message.reply_text(" Failed to generate images.")
        return

    try:
        with open(result["moon_image"], "rb") as f:
            await update.message.reply_photo(photo=f, caption=" Moon")

        with open(result["sky_image"], "rb") as f:
            await update.message.reply_photo(photo=f, caption=" Night Sky")

        await update.message.reply_text(
            " If the moon looks too faded or dark, it's likely a new moon night."
        )

    except Exception as e:
        print(" Error sending images:", e)
        await update.message.reply_text(" Error sending images.")

# Main handler for /sky command
async def sky(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Usage: /sky YYYY-MM-DD [HH:MM:SS]")
        return

    date = args[0]
    time = args[1] if len(args) > 1 else DEFAULT_TIME

    # Reply immediately to avoid timeout
    await update.message.reply_text(f" Generating sky and moon images for {date} {time}...")

    # Run the heavy work in background
    asyncio.create_task(send_images(update, context, date, time))

# Calls Django API
def call_django_api(date, time):
    try:
        res = requests.post(DJANGO_API_URL, json={"date": date, "time": time})
        if res.status_code == 200:
            return res.json()
        else:
            return None
    except Exception as e:
        print("API error:", e)
        return None

# Launches the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sky", sky))

    print(" Telegram bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
