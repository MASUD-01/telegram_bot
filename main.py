from aiogram import Bot, Dispatcher, executor,types
from dotenv import load_dotenv
import openai
import sys
import os

load_dotenv()
openai.api_key=os.getenv('OPENAI_API_KEY')
TELEGRAM_BOT_TOEKN= os.getenv("TELEGRAM_BOT_TOEKN")


class Reference:
    """
    A class to store previous responses from the OpenAI API
    """
    def __init__(self)-> None:
        self.response = ""    #  temporary store response, later we can learn vector databse

reference=Reference()
model_name ="gpt-3.5-turbo"
# Initialize bot and dispatcher
bot= Bot(token=TELEGRAM_BOT_TOEKN)
dispatcher= Dispatcher(bot)

def clear_past():
    '''
    A function to clear the previous converstion and context
    '''
    reference.response=""




@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
        """
            Handler will forward receive a message back to the sender

                 By default, message handler will handle all message types (like a text, photo, sticker etc.)
        """
        clear_past()
        await message.reply('I have clear the past conversation')
    
@dispatcher.message_handler(commands=['start'])
async def clear(message: types.Message):
        """
            Handler will receive
        """
     
        await message.reply('Hi\nI am  tele bot created by masud. How can i assist u')



@dispatcher.message_handler(commands=['help'])
async def clear(message: types.Message):
        """
            A handler to disply the help menu
        """
        help_command = """ Hi There, I am Telegram bot created by masud! Please follow these commands -
         
        /start - to start the conversation and context !
        /help  - to help
        """
        await message.reply(help_command)

@dispatcher.message_handler()
async def chatgpt(message:types.Message):
      """
      A handler to processs ther users input and generate a response using ther chat gpt api
      """

      print(f">>> USER: \n\t{message}")
      response= openai.ChatCompletion.create(
            model=model_name,
            message =[
                  {
                        "role":"assistant","content":reference.response  #   previous converation
                  },
                  {
                        "role":'user',"content": message.text        #current content
                  }
            ]
      )

      reference.response= response['choices'][0]['message']['content']
      print(f">>>chatGPT: \n\t{reference.response}")
      await bot.send_message(chat_id=message.chat.id,text=reference.response)
    
if __name__== "__main__":
     executor.start_polling(dispatcher,skip_updates=True)