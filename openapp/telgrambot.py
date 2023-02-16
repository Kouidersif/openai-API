import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


#first command to start conversation
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, i'm ready to assist you, please ask anything you want!")



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    response = openai.Completion.create(
        model="text-davinci-003",
            prompt=message,
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0,

    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response['choices'][0]['text'])


if __name__ == '__main__':
    application = ApplicationBuilder().token('TELEGRAM_KEY').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()