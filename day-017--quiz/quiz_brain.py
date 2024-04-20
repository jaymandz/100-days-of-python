class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_index = 0
        self.score = 0
    
    def next_question(self):
        cq = self.question_list[self.question_index]
        a = input(f'Q.{self.question_index + 1}: {cq.text} (True/False)?: ')
        self.check_answer(a, cq.answer)
        self.question_index += 1
    
    def still_has_questions(self):
        return self.question_index < len(self.question_list)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_index+1}')
        print()