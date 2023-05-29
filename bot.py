from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ['TELEGRAM_TOKEN']
LINK = os.environ['TELEGRAM_LINK']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    dp.add_error_handler(error)

    updater.start_polling()
