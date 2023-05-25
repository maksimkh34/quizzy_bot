from pysqlitecipher import sqlitewrapper
import api_token
import data
from data import *


db = sqlitewrapper.SqliteCipher(dataBasePath=DB_PATH, checkSameThread=True, password=api_token.db_password)
db.createTable(data.QUIZ_TABLE_NAME, quiz_list, makeSecure=True, commit=True)
