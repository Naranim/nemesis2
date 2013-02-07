__author__ = 'ciemny'

import postgresql.driver as pg_driver
from nemesisTester.config import *

class DB(object) :

    DBdriver = pg_driver.connect(
        user = DB_LOGIN,
        password = DB_PASS,
        host = DB_HOST,
        dabase = DB_NAME,
        port = DB_PORT
    )

