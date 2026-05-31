from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "TOKENNI_KEYIN_QOYAMIZ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti!")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_message))

app.run_polling()
