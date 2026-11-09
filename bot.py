import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ! 🤖 2D smart Assistant Bot မှ ကြိုဆိုပါတယ်။ ဘာများ ကူညီပေးရမလဲ ခင်ဗျာ။")

if __name__ == '__main__':
    #8682983278:AAH1JccHI_GfzHF04oKN-tirupGHNEH6D7o
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    application.run_polling()
