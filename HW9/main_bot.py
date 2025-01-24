from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from llm_handler import generate_response 

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am a bot that can help you with your daily tasks.")

async def process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process the user message."""
    user_message = update.message.text  # Get the user's message
    print(f"Received message: {user_message}")  # Log the message

    llm_response = generate_response(user_message)

    # Clean the response
    assistant_tag = "<|assistant|>"
    if assistant_tag in llm_response:
        llm_response = llm_response.split(assistant_tag, 1)[1].strip()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=llm_response)

def main() -> None:
    print("Hello")
    API_TOKEN = "Enter your API token here"

    application = ApplicationBuilder().token(API_TOKEN).build()
    print("Application created")

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process))
    print("Handlers added")

    print("Running polling")
    application.run_polling()

if __name__ == "__main__":
    print("Running main now")
    main()
