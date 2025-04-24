from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💳 Satın Al", url="https://satin-al-linkin.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Merhaba! Sorularınızı buraya yazabilirsiniz.\n\nSatın almak isterseniz aşağıya tıklayın:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "✅ Sorunuz alındı. En kısa sürede dönüş yapılacaktır.\nSatın almak için /start yazabilirsiniz."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
