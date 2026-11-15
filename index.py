# KY TOKEN - Telegram bot that opens the Mini App
# Install in Pydroid terminal: pip install python-telegram-bot==21.6
# Add your BotFather token and GitHub Pages HTTPS URL below, then run this file.

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "9233065036:AAHflE2ltkqDGpyfKfZZT5hraYx304O_guc"
MINI_APP_URL = "https://kiyaproo-ops.github.io/Ky-token-/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        text="🟢 ورود به KY TOKEN",
        web_app=WebAppInfo(url=MINI_APP_URL)
    )]]
    await update.message.reply_text(
        "🚀 به <b>KY TOKEN</b> خوش آمدی!\n\nبرای باز کردن مینی‌اپ، روی دکمه زیر بزن.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

async def main():
    if BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        raise SystemExit("توکن ربات را در BOT_TOKEN وارد کن.")
    if "YOUR-GITHUB-USERNAME" in MINI_APP_URL:
        raise SystemExit("آدرس واقعی GitHub Pages را در MINI_APP_URL وارد کن.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("KY TOKEN bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Keep the process alive while Pydroid remains running.
    import asyncio
    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
