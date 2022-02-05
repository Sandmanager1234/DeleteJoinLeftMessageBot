import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

from config import (BOT_TOKEN, HEROKU_APP_NAME,
                        WEBHOOK_URL, WEBHOOK_PATH,
                        WEBAPP_HOST, WEBAPP_PORT)

TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(content_types=["new_chat_members"])
async def deleteJoinMessage(msg: types.Message):
    await msg.delete()
@dp.message_handler(content_types=["left_chat_member"])
async def deleteLeftMessage(msg: types.Message):
    await msg.delete()
    
if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )