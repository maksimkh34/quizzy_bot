from telegram import Update
from telegram.ext import ContextTypes
from syss import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'started successfully')
    logl_w(Type.info.value, "New message has received! ")