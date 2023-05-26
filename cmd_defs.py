from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from settings import log
from syss import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Бот запущен! ')
    await help_com(update, context)
    log.logl_w(Type.info.value, f"Bot started at id {update.effective_user.id} ")


async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Команда не распознана! Введите /help для просмотра команд')


async def help_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Разработка ведется (help)')
