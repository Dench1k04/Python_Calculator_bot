import math
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
        # Check for supported operations
        if '+' in expression:
            # Addition operation
            num1, num2 = map(float, expression.split('+'))
            result = num1 + num2
        elif '-' in expression:
            # Subtraction operation
            num1, num2 = map(float, expression.split('-'))
            result = num1 - num2
        elif '*' in expression:
            # Multiplication operation
            num1, num2 = map(float, expression.split('*'))
            result = num1 * num2
        elif '/' in expression:
            # Division operation
            num1, num2 = map(float, expression.split('/'))
            result = num1 / num2
        elif '^' in expression:
            # Exponentiation operation
            num1, num2 = map(float, expression.split('^'))
            result = num1 ** num2
        elif 'abs' in expression:
            # Absolute value operation
            num = float(expression[expression.index('(') + 1:expression.index(')')])
            result = abs(num)
        elif 'mean' in expression:
            # Mean operation
            numbers = expression.split('mean')[1].strip().split(',')
            numbers = [float(num) for num in numbers]
            result = sum(numbers) / len(numbers)
        elif 'sqrt' in expression:
            # Square root operation
            num = float(expression[expression.index('(') + 1:expression.index(')')])
            result = math.sqrt(num)
        else:
            # Unsupported operation
            raise ValueError

        # Send the result back to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))
    except ValueError:
        # Unsupported operation
        context.bot.send_message(chat_id=update.effective_chat.id, text="Unsupported operation. Please try again with a valid expression.")
    except Exception as e:
        # If there is an error, send an error message back to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error! Please try again.")

# Function that will be called when an unknown command is entered
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Function that will be called when the /help command is entered
def help_command(update, context):
    help_text = "This bot is a calculator. Simply type the expression you want to calculate and it will return the result.\n\nAvailable commands:\n/start - Start the bot\n/help - Display this help information"
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

# Get the token of your bot from BotFather
TOKEN = 'your_token_here'
updater = Updater(TOKEN, use_context=True)

# Create handlers for commands
start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)
help_handler = CommandHandler('help', help_command)

# Create handler for evaluating expressions
calc_handler = MessageHandler(Filters.text & (~Filters.command), calculate)

# Add the command and message handlers to the dispatcher
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(calc_handler)

# Start the bot
updater.start_polling()
