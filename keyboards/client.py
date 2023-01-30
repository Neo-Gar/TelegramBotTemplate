from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# TIP: .add() .row() .insert()

# start keyboard
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

start = KeyboardButton('/start')

start_keyboard.add(start)
