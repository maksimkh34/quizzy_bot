from telegram.ext import ApplicationBuilder
from const import API_TOKEN
from settings import log
from syss import Type
import cmd_handlers

log.logl(Type.important.value, "Started! ")

app = ApplicationBuilder().token(API_TOKEN).build()
log.logl(Type.done.value, "App built ")

cmd_handlers.process_handlers(app)
log.logl(Type.done.value, "Handlers processed ")

log.logl(Type.important.value, "Bot preparation completed. Polling started...  ")
app.run_polling()

log.logl(Type.important.value, "Polling closed.  ")
