import time
import asyncpg
from modules.logs.logs import logger


# postgres://user:pass@host:port/database?option=value

class SQL:
    def __init__(self, user, password, host, port, database, enable_logs = None):
        self.dsn = f'postgresql://{user}:{password}@{host}:{port}/{database}'
        self.enable_logs = enable_logs
        self.pool = None

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(self.dsn)

    async def close_pool(self):
        await self.pool.close()

    async def execute(self, execute_query, values = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    await connection.execute(execute_query)
                else:

                    if type(values) is int or type(values) is str:
                        await connection.execute(execute_query, values)
                    else:
                        await connection.execute(execute_query, *values)
        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {execute_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')

    async def executemany(self, execute_query, values = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    await connection.executemany(execute_query)
                else:

                    if type(values) is int or type(values) is str:
                        await connection.executemany(execute_query, values)
                    else:
                        await connection.executemany(execute_query, *values)
        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {execute_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')

    async def fetch(self, fetch_query, values = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    return await connection.fetch(fetch_query)
                else:

                    if type(values) is int or type(values) is str:
                        return await connection.fetch(fetch_query, values)
                    else:
                        return await connection.fetch(fetch_query, *values)

        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {fetch_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')

    async def fetchrow(self, fetch_query, values = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    return await connection.fetchrow(fetch_query)

                else:

                    if type(values) is int or type(values) is str:
                        return await connection.fetchrow(fetch_query, values)
                    else:

                        return await connection.fetchrow(fetch_query, *values)

        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {fetch_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')

    async def fetchval(self, fetch_query, values = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    return await connection.fetchval(fetch_query)

                else:

                    if type(values) is int or type(values) is str:
                        return await connection.fetchval(fetch_query, values)

                    else:
                        return await connection.fetchval(fetch_query, *values)

        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {fetch_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')

    async def execute_and_getlastid(self, execute_query, values = None,
                                    table_name: str | None = None):
        try:
            if self.enable_logs:
                start_time = time.time()
                logger.debug('[SQL] [TRY]')
            async with self.pool.acquire() as connection:

                if values is None:
                    await connection.execute(execute_query)
                    fetch = await connection.fetchval(
                        f'SELECT LASTVAL() FROM {table_name}'
                    )
                    return fetch
                else:

                    if type(values) is int or type(values) is str:
                        await connection.execute(execute_query, values)
                        fetch = await connection.fetchval(
                            f'SELECT LASTVAL() FROM {table_name}'
                        )
                        return fetch
                    else:
                        await connection.execute(execute_query, *values)
                        fetch = await connection.fetchval(
                            f'SELECT LASTVAL() FROM {table_name}'
                        )
                        return fetch
        except Exception:
            logger.error(f'[SQL] [CONNECTION REFUSED!] [QUERY]: {execute_query} [VALUES]: {values}', exc_info=True)
        finally:
            if self.enable_logs:
                logger.debug(f'[SQL] [DONE] [DONE IN {time.time() - start_time}]')
