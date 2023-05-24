from quiz import *


def answer(answer_, quiz_):
    print(f"Trying to: answer question \'{quiz_.get_current_question().get_name()}\' ({answer_}): "
          f"{quiz_.try_answer(answer_)}")
    print(f"Quiz status: {quiz_.get_quiz_status()} out of {len(quiz_.questions)} are correct. ")
    print()


FirstQ = Question("Number of this question? ", True, "First")
SecondQ = Question("Number of this question (2)? ", False, "Second")

ThirdQ = TestQuestion("How many answers in this quiz? ", False, "3", "1", "2", "3")

mainQuiz = Quiz(FirstQ, SecondQ, ThirdQ)

for i in range(0, len(mainQuiz.questions)):
    if mainQuiz.try_answer(input(f"{mainQuiz.get_current_question().get_name()} ")):
        print("Correct! ")
    else:
        print("Wrong answer... ")
print(f"Quiz is completed. Correct answers: {mainQuiz.correct_answers()} out of {len(mainQuiz.questions)} "
      f"({int(round(mainQuiz.get_results(), 2)*100)}%)")
