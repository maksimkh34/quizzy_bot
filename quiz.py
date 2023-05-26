import id_generator
import settings


class Question:
    text = ""
    correct_answers = []
    creator = ""
    is_rounding = False
    correct = False

    def __init__(self, _text, is_rounding, *_correct_answers):

        self.text = _text
        self.is_rounding = is_rounding
        self.correct_answers = list(_correct_answers)

    def import_question(self, strq) -> None:
        if strq.split(":")[0] == "DQue":
            self.correct_answers.clear()
            self.text = strq.split(":")[2].split(";")[0]
            for answer_ in strq.split(":")[2].split(";")[1:]:
                self.correct_answers.append(answer_)
            if strq.split(":")[1] == "Y":
                self.is_rounding = True
            self.correct_answers.pop()

    def ans(self, text) -> str:
        if self.is_rounding:
            return text.lower()
        else:
            return text

    def ans_list(self, list_) -> []:
        if self.is_rounding:
            new_list = []
            for string in list_:
                new_list.append(string.lower())
            return new_list
        else:
            return list_

    def try_to_answer(self, answer) -> bool:
        self.correct = self.ans(answer) in self.ans_list(self.correct_answers)
        return self.correct

    def get_name(self) -> str:
        return self.text

    def get_string(self) -> str:
        rounding = "F"
        if self.is_rounding:
            rounding = "Y"
        output = f"DQue:{rounding}:{self.get_name()};"
        for ans_ in self.correct_answers:
            output += f"{ans_};"
        return output


class TestQuestion(Question):
    answers = []

    def __init__(self, _text, is_rounding, _correct_answer, *_answers):
        super().__init__(_text, is_rounding, _correct_answer)
        self.answers = list(_answers)

    def get_string(self) -> str:
        output = f"TQue:{self.get_name()}:{self.correct_answers[0]}:"
        for answer_ in self.answers:
            output += f"{answer_};"
        return output

    # TQue:Which?:2:1;2;3
    def import_question(self, strq) -> None:
        list_ = strq.split(":")
        if list_[0] == "TQue":
            self.text = list_[1]
            self.correct_answers.clear()
            self.correct_answers.append(list_[2])
            self.answers.clear()
            for ans in list_[3].split(";"):
                if ans != "":
                    self.answers.append(ans)


class Quiz:
    questions = []
    current_question = 0
    completed = False
    name = ""
    id = ""

    def __init__(self, name: str, id_: str, creator: str, *_questions: Question):
        self.creator = creator
        self.id = id_
        self.id = id_generator.generate_id([])
        self.name = name
        self.questions = list(_questions)

    def get_sqlready_string(self) -> []:
        return [self.name, self.id, self.get_string(), self.creator]

    def import_quiz(self, sql_data: []) -> None:
        self.name = sql_data[0]
        self.id = sql_data[1]
        self.import_answers(sql_data[2])
        self.creator = sql_data[3]

    def add_question(self, q) -> None:
        self.questions.append(q)

    def get_correct_answers(self) -> int:
        correct = 0
        for q in self.questions:
            if q.correct:
                correct += 1
        return correct

    def import_answers(self, stra) -> None:
        list_ = stra.split("^")
        if list_[0] == "Q":
            self.questions.clear()
            for que in list_[1:]:
                if que.split(":")[0] == "DQue":
                    temp = Question("", False, "")
                    temp.import_question(que)
                    self.questions.append(temp)
                else:
                    temp = TestQuestion("", False, "", "")
                    temp.import_question(que)
                    self.questions.append(temp)

    def get_string(self) -> str:
        output = "Q^"
        for question in self.questions:
            output += question.get_string() + "^"
        output = output[:-1]
        return output

    def try_answer(self, answer_) -> bool:
        correct = self.questions[self.current_question].try_to_answer(answer_)
        self.questions[self.current_question].correct = correct
        if self.current_question == (len(self.questions) - 1):
            self.completed = True
        else:
            self.current_question += 1
        return correct

    def get_current_question(self) -> Question:
        return self.questions[self.current_question]

    def get_results(self) -> float:
        if self.completed:
            return float(self.get_correct_answers() / len(self.questions))

