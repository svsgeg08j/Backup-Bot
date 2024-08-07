import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv('7330107332:AAGi6vu9SIYe7iTqmLGKmAnr8gGefjk7Kag')
TARGET_CHAT_ID = os.getenv('4273472589')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I am your media forwarding bot.')

def forward_media(update: Update, context: CallbackContext) -> None:
    message = update.message

    if message.photo:
        context.bot.send_photo(chat_id=TARGET_CHAT_ID, photo=message.photo[-1].file_id)
    elif message.video:
        context.bot.send_video(chat_id=TARGET_CHAT_ID, video=message.video.file_id)
    elif message.document:
        context.bot.send_document(chat_id=TARGET_CHAT_ID, document=message.document.file_id)
    elif message.audio:
        context.bot.send_audio(chat_id=TARGET_CHAT_ID, audio=message.audio.file_id)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video | Filters.document | Filters.audio, forward_media))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
