
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command ပို့လိုက်သည့်အခါ ပြန်မည့် မက်ဆေ့ချ်
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "🤖 မင်္ဂလာပါ! 2D smart Assistant မှ ကြိုဆိုပါတယ်။\n\n"
        "📲 **Official Channel:** @HTETAUNG2D2D\n"
        "📲 **Second Channel:** @HTETAUNG2DD2\n"
        "📞 **Phone:** 09401587917\n\n"
        "အချက်အလက်များကို သိရှိလိုပါက ဆက်သွယ်နိုင်ပါသည်။"
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

# အခြားစာသားများ ပို့လာပါက တုံ့ပြန်ရန်
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response_message = (
        "မင်္ဂလာပါရှင့်/ဗျာ 🙏\n\n"
        "• Official Channel: @HTETAUNG2D2D\n"
        "• Second Channel: @HTETAUNG2DD2\n"
        "• Phone: 09401587917\n\n"
        "အသေးစိတ်ကို ဆက်သွယ်စုံစမ်းနိုင်ပါသည်။"
    )
    await update.message.reply_text(response_message)

if __name__ == '__main__':
    # Bot Token ထည့်သွင်းခြင်း
    token = "8682983278:AAH81HLMrbrxU9qEKOjM5Tv9NKH1Lv2w9Nc"
    application = ApplicationBuilder().token(token).build()

    # Handlers များ ချိတ်ဆက်ခြင်း
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    application.run_polling()
