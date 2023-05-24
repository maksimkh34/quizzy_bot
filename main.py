from telegram.ext import ApplicationBuilder
from api_token import API_TOKEN
from syss import log, logl, Type
import cmd_handlers


logl(Type.important.value, "Started! ")

app = ApplicationBuilder().token(API_TOKEN).build()
logl(Type.done.value, "App built ")
cmd_handlers.process_handlers(app)
logl(Type.done.value, "Handlers processed ")
logl(Type.important.value, "Bot preparation completed. Polling started...  ")
app.run_polling()

logl(Type.important.value, "Bot closed.  ")
