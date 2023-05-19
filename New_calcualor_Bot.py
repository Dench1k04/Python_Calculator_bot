import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Function that will be called when the /start command is entered
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a calculator. Type the expression you want me to calculate.")

# Function that will be called when an expression is entered
def calculate(update, context):
    # Get the expression entered by the user
    expression = update.message.text

    try:
        # Try to evaluate the expression
        result = eval(expression)
        # Send the result back to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))
    except:
        # If there is an error, send an error message back to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error! Please try again.")

# Function that will be called when an unknown command is entered
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Function that will be called when the /help command is entered
def help_command(update, context):
    help_text = "This bot is a calculator. Simply type the expression you want to calculate and it will return the result.\n\nAvailable commands:\n/start - Start the bot\n/help - Display this help information"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

# Function that will be called when an unsupported operation is entered
def unsupported_operation(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Unsupported operation. Please try again with a valid expression.")

# Get the token of your bot from BotFather
TOKEN = 'your_token_here'
updater = Updater(TOKEN, use_context=True)

# Create handlers for commands
start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)
help_handler = CommandHandler('help', help_command)

# Create handler for evaluating expressions
calc_handler = MessageHandler(Filters.text & (~Filters.command), calculate)

# Create handler for unsupported operations
unsupported_handler = MessageHandler(Filters.text & Filters.regex(r'.*\W+.*'), unsupported_operation)

# Add the command and message handlers to the dispatcher
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(unsupported_handler)

# Start the bot
updater.start_polling()
