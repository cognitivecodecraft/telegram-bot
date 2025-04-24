from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackContext,
    CallbackQueryHandler
)
import os

TOKEN = os.getenv("BOT_TOKEN")

# Paket verileri
packages = {
    "basic": {
        "name": "🎯 Basic Paket",
        "features": "✅ Özellik 1\n✅ Özellik 2\n\n💰 Fiyat: 10 USDT",
        "wallet": "TRC20: TXabc123..."
    },
    "plus": {
        "name": "🚀 Basic Plus Paket",
        "features": "✅ Tüm Basic özellikleri\n✅ Ekstra Özellik\n\n💰 Fiyat: 25 USDT",
        "wallet": "TRC20: TXdef456..."
    },
    "pro": {
        "name": "👑 Pro Paket",
        "features": "✅ Tüm özellikler\n✅ VIP Destek\n\n💰 Fiyat: 50 USDT",
        "wallet": "TRC20: TXghi789..."
    }
}

# /start komutu
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎯 Basic", callback_data="basic")],
        [InlineKeyboardButton("🚀 Basic Plus", callback_data="plus")],
        [InlineKeyboardButton("👑 Pro", callback_data="pro")]
    ]
    await update.message.reply_text(
        "👋 Hoş geldiniz!\n\nAşağıdan bir paket seçiniz:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Paket seçimi sonrası gösterilecek içerik
async def handle_package_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    package_id = query.data
    pkg = packages[package_id]

    msg = f"""
{pkg['name']}

{pkg['features']}

🪙 Ödeme için cüzdan adresi:
{pkg['wallet']}

💬 Ödeme yaptıktan sonra size özel bir **kod** gönderilecektir.

🔎 Detaylı bilgi için: https://cognitivecodecraft.store
"""
    await query.edit_message_text(msg)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_package_selection))
    app.run_polling()

if __name__ == "__main__":
    main()
