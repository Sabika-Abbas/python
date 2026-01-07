import random
import sys
import ast  # Safer alternative to eval

class Question:
    def __init__(self):
        self.question = [None, [], None]
    
    def setQuestion(self, qs):
        self.question[0] = qs
    
    def setOptions(self, op1, op2, op3):
        self.question[1] = [op1, op2, op3]  # Clear existing options first
    
    def setAnswer(self, n):
        self.question[2] = n
    
    def printQuestionWithAnswer(self):
        print(self.question[0])
        print('a.', self.question[1][0])
        print('b.', self.question[1][1])
        print('c.', self.question[1][2])
        print('Correct answer is', self.question[1][self.question[2]-1])
    
    def printQuestion(self):
        print(self.question[0])
        print('a.', self.question[1][0])
        print('b.', self.question[1][1])
        print('c.', self.question[1][2])
    
    def checkAnswer(self, ans):
        key = {'a':1, 'b':2, 'c':3}
        return ans.lower() in key and self.question[2] == key[ans.lower()]
    
    def __str__(self):
        return str(self.question)

class QuestionDB:
    def __init__(self):
        self.questionList = []
        self.loadQuestionList()
    
    def addQuestion(self):
        q = Question()
        x = input('\nEnter question: ')
        q.setQuestion(x)
        x1 = input('Enter option 1: ')
        x2 = input('Enter option 2: ')
        x3 = input('Enter option 3: ')
        q.setOptions(x1, x2, x3)
        
        while True:
            try:
                x = int(input('Enter answer (1, 2 or 3): '))
                if 1 <= x <= 3:
                    q.setAnswer(x)
                    self.questionList.append(q)
                    break
                else:
                    print('Please enter 1, 2, or 3!')
            except ValueError:
                print('Invalid input! Please enter a number.')
    
    def printQuestionList(self):
        for ID, question in enumerate(self.questionList, 1):
            print(f'\nQID: {ID}')
            question.printQuestionWithAnswer()
    
    def removeQuestion(self):
        try:
            ID = int(input('Enter QID to remove: '))
            if 1 <= ID <= len(self.questionList):
                self.questionList.pop(ID-1)
                print('Question removed successfully!')
            else:
                print('Invalid QID!')
        except ValueError:
            print('Please enter a valid number!')
    
    def saveQuestionList(self):
        with open('QuestionsDB.txt', 'w') as f:
            for question in self.questionList:
                f.write(str(question) + '\n')
    
    def loadQuestionList(self):
        self.questionList = []
        try:
            with open('QuestionsDB.txt', 'r') as f:
                for line in f:
                    try:
                        # Using ast.literal_eval instead of eval for safety
                        question_data = ast.literal_eval(line.strip())
                        q = Question()
                        q.setQuestion(question_data[0])
                        q.setOptions(*question_data[1])
                        q.setAnswer(question_data[2])
                        self.questionList.append(q)
                    except:
                        print(f"Warning: Skipping invalid question data: {line}")
                        continue
            return True
        except FileNotFoundError:
            return False

class Quiz:
    def __init__(self):
        self.QDB = QuestionDB()
        if len(self.QDB.questionList) < 5:
            print("Error: Need at least 5 questions in the database!")
            return
        
        self.selectedQuestionsList = []
        self.score = 0
        self.makeQuiz()
        self.takeQuiz()
        self.printScore()
    
    def makeQuiz(self):
        self.selectedQuestionsList = random.sample(self.QDB.questionList, min(5, len(self.QDB.questionList)))
    
    def takeQuiz(self):
        for i, question in enumerate(self.selectedQuestionsList, 1):
            print(f'\nQuestion #{i}:')
            question.printQuestion()
            while True:
                answer = input('Enter answer (a, b or c): ').lower()
                if answer in ['a', 'b', 'c']:
                    break
                print("Invalid input! Please enter a, b, or c.")
            
            if question.checkAnswer(answer):
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
    
    def printScore(self):
        print(f'\nYour score: {self.score} out of {len(self.selectedQuestionsList)}')

class UserInterface:
    def __init__(self):
        while True:
            self.displayMainMenu()
            choice = input('Enter option number: ')
            if choice == '1':
                self.editQuiz()
            elif choice == '2':
                Quiz()
            else:
                break
    
    @staticmethod
    def displayMainMenu():
        print('\n' + '*'*27)
        print('1. Edit question database')
        print('2. Take quiz')
        print('Press any other key to exit')
        print('*'*27)
    
    @staticmethod
    def displayEditMenu():
        print('\n' + '^'*28)
        print('1. List questions')
        print('2. Add question')
        print('3. Remove question')
        print('4. Save changes')
        print('5. Go back to main menu')
        print('Press any other key to exit')
        print('^'*28)
    
    def editQuiz(self):
        QDB = QuestionDB()
        while True:
            self.displayEditMenu()
            choice = input('Enter option number: ')
            if choice == '1':
                QDB.printQuestionList()
            elif choice == '2':
                QDB.addQuestion()
            elif choice == '3':
                QDB.removeQuestion()
            elif choice == '4':
                QDB.saveQuestionList()
                print('Changes saved successfully!')
            elif choice == '5':
                break
            else:
                sys.exit()

# Driver Code
if __name__ == "__main__":
    print("=== Quiz Application ===")
    
    # Initialize database
    qdb = QuestionDB()
    
    # Add sample questions if database is empty
    if not qdb.questionList:
        print("\nCreating sample questions...")
        sample_questions = [
            ("What is the capital of France?", ["London", "Paris", "Berlin"], 2),
            ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter"], 2),
            ("What is 2 + 2?", ["3", "4", "5"], 2),
            ("Which language is this program written in?", ["Java", "C++", "Python"], 3),
            ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2)
        ]
        
        for q_text, options, ans in sample_questions:
            q = Question()
            q.setQuestion(q_text)
            q.setOptions(*options)
            q.setAnswer(ans)
            qdb.questionList.append(q)
        
        qdb.saveQuestionList()
        print("Added 5 sample questions to the database.")
    
    # Start the user interface
    UserInterface()