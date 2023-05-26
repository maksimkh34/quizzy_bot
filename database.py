from pysqlitecipher import sqlitewrapper
import const
import data


class Database:
    db = None

    def __init__(self, path, password):
        self.db = sqlitewrapper.SqliteCipher(
            dataBasePath=path, checkSameThread=True, password=password)

    def get_taken_ids(self):
        ids = []
        try:
            quizzes = self.import_quizzes()[1:]
        except ValueError:
            return []
        for quiz in quizzes:
            ids.append(quiz[1])
        return ids

    def import_quizzes(self, omitId=True):
        return self.db.getDataFromTable(data.QUIZ_TABLE_NAME, omitId, omitID=omitId)[1]

    def append_quiz(self, quiz):
        self.db.insertIntoTable(data.QUIZ_TABLE_NAME, quiz.get_sqlready_string(), commit=True)

    def init_db(self):
        self.db.createTable(data.QUIZ_TABLE_NAME, data.quiz_list, makeSecure=True, commit=True)

    def get_ids(self):
        quizzes = self.import_quizzes(False)
        ids = []
        for quiz in quizzes:
            ids.append(quiz[0])
        return ids

    def clear(self):
        for i in self.get_ids():
            self.db.deleteDataInTable(data.QUIZ_TABLE_NAME, i, commit=True, updateId=False, raiseError=True)

    def remove(self, id_):
        quizzes = self.import_quizzes(False)
        for quiz in quizzes:
            if quiz[2] == id_:
                self.db.deleteDataInTable(data.QUIZ_TABLE_NAME, quiz[0], commit=True, updateId=True, raiseError=True)

    # user database functional

    def init_db_usr(self):
        self.db.createTable(data.USR_TABLE_NAME, data.usr_list, makeSecure=True)

    def u_insert(self, user_id: str):
        self.db.insertIntoTable(data.USR_TABLE_NAME, [user_id])

    def u_get_list(self):
        return self.db.getDataFromTable(data.USR_TABLE_NAME)

    def u_clear(self):
        for i in range(len(self.u_get_list()[1])):
            self.db.deleteDataInTable(data.USR_TABLE_NAME, i, commit=True, updateId=False, raiseError=True)
            i += 1
