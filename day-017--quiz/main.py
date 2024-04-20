from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz = QuizBrain(
    [Question(q['text'], q['answer']) for q in question_data]
)

while quiz.still_has_questions(): quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Your final score was: {quiz.score}/{len(quiz.question_list)}')