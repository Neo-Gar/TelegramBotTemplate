from colorama import Fore, init
from aiogram import executor
from aiogram.types.input_file import InputFile
from create_bot import dp, bot
from modules.logs.logs import logger
from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime
import os

from handlers.client import register_handlers_client

init()

parser = ArgumentParser()
parser.add_argument('-debug',
                    action='store_true',
                    default=False,
                    help='runs bot in debug mode')
parser.add_argument('-polling',
                    action='store_true',
                    default=False,
                    help='runs bot in long-polling mode')
args = parser.parse_args()

DEBUG_MODE = args.debug
LONG_POLLING = args.polling

print(f'DEBUG_MODE={DEBUG_MODE}')
print(f'LONG_POLLING={LONG_POLLING}')


async def on_startup(_):
    async def set_webhook():
        print(Fore.YELLOW + 'Setting webhook...')
        await bot.set_webhook(
            url=os.getenv('WEBHOOK_HOST') + ':' + os.getenv('WEBAPP_PORT') + os.getenv('WEBHOOK_PATH'),
            ip_address=os.getenv('WEBHOOK_HOST'),
            certificate=InputFile(Path(os.getenv('SSL_PATH_TO_PEM'))))

    if LONG_POLLING is False:
        await set_webhook()

    print(Fore.GREEN + 'Bot is online!')
    print(Fore.YELLOW + f'Startup time: {str(datetime.now())}')
    print(Fore.RESET)
    logger.info('Bot is online!')
    logger.info(f'Startup time: {str(datetime.now())}')


async def on_shutdown(_):
    print(Fore.RED + 'Shutting down...')
    if LONG_POLLING is False:
        await bot.delete_webhook()


# register handlers
register_handlers_client(dp)


# startup
if __name__ == '__main__':
    if LONG_POLLING is True:
        # long-polling
        executor.start_polling(dp,
                               skip_updates=True,
                               on_startup=on_startup,
                               on_shutdown=on_shutdown)
    else:
        # webhook
        executor.start_webhook(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            webhook_path=os.getenv('WEBHOOK_PATH'),
            host=os.getenv('WEBAPP_HOST'),
            port=os.getenv('AIOHTTP_PORT')
        )
