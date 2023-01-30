from aiogram import types
from os import getenv
from modules.logs.logs import logger


async def admin_check(message: types.Message):
    if message.from_user.id == int(getenv('ADMIN_ID')):
        logger.info(f'User: "{message.from_user.full_name}"'
                    f' ID: "{message.from_user.id}" PASSED admin_check')
        return True
    elif message.from_user.id != int(getenv('ADMIN_ID')):
        await message.answer('Вы не являетесь администратором')
        logger.info(f'User: "{message.from_user.full_name}"'
                    f' ID: "{message.from_user.id} FAILED admin_check')
        return False
    else:
        logger.error('ERROR', stack_info=True)
        return False
