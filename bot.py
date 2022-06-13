import os
from telegram.ext import Updater, MessageHandler, Filters


def process_message(update, context):

    text = update.message.text

    if str(text).__contains__('-1001590309863'):
        context.bot.send_message(
            chat_id='-1001590309863',
            text=str(text).replace('-1001590309863', '-1001590309863')
        )


if __name__ == '__main__':

    updater = Updater(token=('5327523213:AAFwwijRyEXsTKChHHZemT_jfh-ugLHCy-c'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()
