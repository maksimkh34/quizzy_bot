from telegram.ext import ApplicationBuilder

import cmd_handlers
import token

app = ApplicationBuilder().token(token.API_TOKEN).build()
cmd_handlers.process_handlers(app)
app.run_polling()
