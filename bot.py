from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8939218526:AAGsNc08cgzq1hUrQvw4oTXlwYuBj-1zjp4"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("shu kanallarga obuna boling https://www.youtube.com/@Vampires_play!")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_message))

app.run_polling()
