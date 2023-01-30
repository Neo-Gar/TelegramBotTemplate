from os import getenv
from dotenv import load_dotenv, find_dotenv
from modules.postgresql_core import SQL
from modules.logs.logs import logger, ENABLE_CORE_SQL_LOGS


load_dotenv(find_dotenv())

sql = SQL(
    host=getenv('DB_HOST'),
    port=getenv('DB_PORT'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    database=getenv('DB_NAME'),
    enable_logs=ENABLE_CORE_SQL_LOGS
)


async def client_pool():
    await sql.create_pool()


async def close_client_pool():
    await sql.close_pool()
