from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from cmd_defs import *


def process_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_com))

    app.add_handler(CallbackQueryHandler(query_handler))

    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))
