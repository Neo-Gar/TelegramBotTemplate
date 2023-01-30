from aiogram import types, Dispatcher
from modules.logs.logs import logger
from create_bot import bot

from keyboards.client import start_keyboard


async def cmd_start(message: types.Message):
    logger.info(f'[TRY] {message}')

    await message.answer(
        'Template bot!',
        reply_markup=start_keyboard
    )

    logger.info(f'[DONE] {message}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
