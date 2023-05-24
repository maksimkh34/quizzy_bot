class Question:
    text = ""
    correct_answers = []
    is_rounding = False
    correct = False

    def __init__(self, _text, is_rounding, *_correct_answers):
        self.text = _text
        self.is_rounding = is_rounding
        self.correct_answers = _correct_answers

    def ans(self, text):
        if self.is_rounding:
            return text.lower()
        else:
            return text

    def ans_list(self, list_):
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

    def get_name(self):
        return self.text


class TestQuestion(Question):
    answers = []

    def __init__(self, _text, is_rounding, _correct_answer, *_answers):
        super().__init__(_text, is_rounding, _correct_answer)
        self.answers = _answers


class Quiz:
    questions = []
    current_question = 0
    completed = False

    def __init__(self, *_questions):
        self.questions = list(_questions)

    def add_question(self, q):
        self.questions.append(q)

    def correct_answers(self):
        correct = 0
        for q in self.questions:
            if q.correct:
                correct += 1
        return correct

    def try_answer(self, answer_):
        correct = self.questions[self.current_question].try_to_answer(answer_)
        self.questions[self.current_question].correct = correct
        if self.current_question == (len(self.questions) - 1):
            self.completed = True
        else:
            self.current_question += 1
        return correct

    def get_current_question(self) -> Question:
        return self.questions[self.current_question]

    def get_results(self):
        if self.completed:
            return float(self.correct_answers()/len(self.questions))
