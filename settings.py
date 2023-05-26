import const
import data
import database
import syss

# settings file is used to store vars or objects that have to be used in the entire program

db = database.Database(data.DB_PATH, const.db_password)  # DB to work with (in program)
usr_db = database.Database(data.USER_DB_PATH, const.usr_db_password)

log = syss.Logger()