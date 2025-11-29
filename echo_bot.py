import logging
from aiogram import Bot, Dispatcher, executor,types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOEKN= os.getenv("TELEGRAM_BOT_TOEKN")
# print(TELEGRAM_BOT_TOEKN)

#configure logging
logging.basicConfig(level=logging.INFO)

#Iniitialize bot and dispatcher
bot= Bot(token=TELEGRAM_BOT_TOEKN)
dp= Dispatcher(bot)

@dp.message_handler()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    
    await message.answer(message.text)


if __name__ == "__main__":
   executor.start_polling(dp,skip_updates=True)