from telegram.ext import CommandHandler
from cmd_defs import *


def process_handlers(app):
    app.add_handler(CommandHandler("start", start))
