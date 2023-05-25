from quiz import *

q1 = Question("How many? ", True, "1", "2")
q2 = Question("How many?2  ", True, "1", "2")
q3 = TestQuestion("How many?3 ", True, "2", "2", "3", "1")
quiz = Quiz("test1", q1, q2, q3)
str_ = quiz.get_string()
print(str_)
quiz2 = Quiz("test2")
quiz2.import_answers(str_)
print(quiz2.get_string())
