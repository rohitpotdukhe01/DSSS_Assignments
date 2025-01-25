from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from llm_handler import generate_response 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello! I am a bot that can help you with your daily tasks.")

async def process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    print(f"Received message: {user_message}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"I am processing your message : {user_message}")

    llm_response = generate_response(user_message)
    assistant_tag = "<|assistant|>"
    if assistant_tag in llm_response:
        llm_response = llm_response.split(assistant_tag, 1)[1].strip()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=llm_response)

def main() -> None:
    print("Hello")    
    API_TOKEN = "7811652764:AAHsGZovSBazla9io-cIqZd1kgGygabclb4"

    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process))

    application.run_polling()

if __name__ == "__main__":
    main()