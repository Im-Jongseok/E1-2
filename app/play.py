from Quiz import Quiz
from utils import get_valid_input, print_double_line, print_line

global top_score
top_score = -1

def play(quizzes): 
    if not quizzes:
        print("EMPTY QUIZ ERROR: 퀴즈가 없습니다. 퀴즈를 추가해주세요.\n")
        return
    score = 0

    print_line()
    print(f"퀴즈를 시작합니다!(총 {len(quizzes)}문제)")
    print_line()

    for quiz in quizzes:
        print_quiz(quiz)
        score = player_score(quiz, score)
    print_score(len(quizzes), score)


def print_quiz(quiz):
    print(quiz.question + "\n")

    for i, choice in enumerate(quiz.choices):
        print(f"{i+1}. {choice}")
    print() 


def player_score(quiz, score):
    player_answer = get_valid_input(1, len(quiz.choices), "정답 입력: ")
    
    if quiz.check_answer(player_answer):
        print("정답입니다!\n")
        score += 1
    else:
        print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.\n")
    print_line()
    return score


def print_score(quiz_len, score):
    print_double_line()
    point = int(score / quiz_len * 100)
    print(f"결과: {quiz_len}문제 중 {score}문제 정답! ({point}점)\n")
    if is_top_score(point):
        print("새로운 최고 점수입니다!\n")
    print_double_line()


def add_quiz(quizzes):
    print("\n새로운 퀴즈를 추가합니다.\n")
    question = input("문제를 입력하세요: ")         # question 
    choices = []                                # choices
    for i in range(4):                          
        choice = input(f"선택지 {i+1}: ")
        choices.append(choice)
    answer = get_valid_input(1, 4, "정답 번호 (1-4): ")    # answer

    new_quiz = Quiz(question, choices, answer) # Quiz 클래스의 인스턴스로 퀴즈 생성
    quizzes.append(new_quiz)
    print("퀴즈가 추가되었습니다!\n")


def print_quiz_list(quizzes):
    print_line()
    print(f"등록된 퀴즈 목록 (총 {len(quizzes)}문제):\n")
    print_line()

    for i, quiz in enumerate(quizzes):
        print(f"[{i+1}] {quiz.question}")
    print_line()


def is_top_score(score):
    global top_score
    
    if top_score < score:
        top_score = score
        return 1
    return 0
    

def print_top_score(_len_quizzes):
    if top_score == -1:
        print("EMPTY SCORE ERROR: 점수가 없습니다.\n")
        return
    score = int((top_score / 100) * _len_quizzes)
    print(f"최고 점수: {top_score} 점 ({_len_quizzes}문제 중 {score}문제 정답)\n")