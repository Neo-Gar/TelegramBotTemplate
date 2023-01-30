import pymysql
from colorama import Fore, init
from modules.logs.logs import logger

init()


class SQL:
    def __init__(self, host, port, user, password, database,
                 enable_logs: bool | None = None):
        self.connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
            )
        self.enable_logs = enable_logs

    def create_table(self, create_table_query):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY create_table')
                with self.connection.cursor() as cursor:
                    cursor.execute(create_table_query)
                    if self.enable_logs is True:
                        logger.debug('SQL: create_table SUCCESS')

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {create_table_query}', exc_info=True)

    def insert(self, insert_query,
               values=None,
               get_last_insert_id: bool | None = None,
               row: str | None = None,
               table: str | None = None):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY insert')
                with self.connection.cursor() as cursor:
                    cursor.execute(insert_query, values)
                    self.connection.commit()
                    if self.enable_logs is True:
                        logger.debug('SQL: insert SUCCESS')

                    if get_last_insert_id is True:
                        if self.enable_logs is True:
                            logger.debug('SQL: TRY select_last_insert_id')
                        select_last_insert_id = f'SELECT `{row}` FROM {table} ' \
                                                f'WHERE `{row}` = LAST_INSERT_ID();'
                        cursor.execute(select_last_insert_id)
                        if self.enable_logs is True:
                            logger.debug('SQL: select_last_insert_id SUCCESS')
                        return cursor.fetchone()

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {insert_query} [VALUES] {values}', exc_info=True)

    def update(self, update_query,
               values=None):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY update')
                with self.connection.cursor() as cursor:
                    cursor.execute(update_query, values)
                    self.connection.commit()
                    if self.enable_logs is True:
                        logger.debug('SQL: update SUCCESS')

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {update_query} [VALUES] {values}', exc_info=True)

    def delete(self, delete_query):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY delete')
                with self.connection.cursor() as cursor:
                    cursor.execute(delete_query)
                    self.connection.commit()
                    if self.enable_logs is True:
                        logger.debug('SQL: delete SUCCESS')

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {delete_query}', exc_info=True)

    def select_one(self, select_one_query,
                   values=None):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY select_one')
                with self.connection.cursor() as cursor:
                    cursor.execute(select_one_query, values)
                    if self.enable_logs is True:
                        logger.debug('SQL: select_one SUCCESS')
                    return cursor.fetchone()

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {select_one_query} [VALUES] {values}', exc_info=True)

    def select_all(self, select_all_query,
                   values=None):
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY select_all')
                with self.connection.cursor() as cursor:
                    cursor.execute(select_all_query, values)
                    if self.enable_logs is True:
                        logger.debug('SQL: select_all SUCCESS')
                    return cursor.fetchall()

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {select_all_query} [VALUES] {values}', exc_info=True)

    def truncate(self, truncate_query): # sql-injection vulnerability!!!
        try:
            self.connection.connect()
            if self.enable_logs is True:
                logger.debug('Successfully connected to SQL...')
            try:
                if self.enable_logs is True:
                    logger.debug('SQL: TRY truncate')
                with self.connection.cursor() as cursor:
                    cursor.execute(truncate_query)
                    self.connection.commit()
                    if self.enable_logs is True:
                        logger.debug('SQL: truncate SUCCESS')

            finally:
                self.connection.close()
                if self.enable_logs is True:
                    logger.debug('Closing connection...')

        except Exception:
            logger.error(f'[Connection refused] [QUERY] {truncate_query}', exc_info=True)
