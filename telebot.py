import logging
import telegram 
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
LOCATION, PHOTO, NAME, SERVING, TIME, CONFIRMATION = range(6)
reply_keyboard = [['شروع دوباره', 'مورد تایید است']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
TOKEN = "1860656815:AAH8hs32fC5WK4jImhGQJMLnSQEuyEKAmOs"
bot = telegram.Bot(token=TOKEN)
chat_id = "@Aliparsi"
PORT = int(os.environ.get('PORT', 5000))  

def start(update, context):
    user = update
    print(user)

def main():
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN)
    updater.bot.set_webhook('https://d4e3a29ea3c6.ngrok.io/' + TOKEN)
    updater.idle()
if __name__ == '__main__':
    main()
