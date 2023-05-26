DB_PATH = "quiz.db"
USER_DB_PATH = "usr.db"

LOG_FILE_PATH = "log.txt"

QUIZ_TABLE_NAME = "Quiz"
quiz_list = [
    ["name", "TEXT"],
    ["id", "TEXT"],
    ["questions", "TEXT"],
    ["creator", "TEXT"]
]

USR_TABLE_NAME = "User"
usr_list = [
    ["userid", "TEXT"]
]

# data file is used for storing vars or objects that can be changed in-dev
